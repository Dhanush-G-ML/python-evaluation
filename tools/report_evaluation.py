"""Generate an Excel-ready evaluation CSV for the four mentees."""

import argparse
from collections import Counter, defaultdict
import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import re
import subprocess
import sys
from xml.etree import ElementTree

from review_submission import (
    CheckResult,
    EXERCISE_MODULE,
    expected_programs,
    review_program_exercise,
    review_test_exercise,
)


ROOT = Path(__file__).resolve().parents[1]
MENTEES = {
    "rishitaa-bohra": "Rishitaa Bohra",
    "sahana-n": "Sahana N",
    "dhanya-arun": "Dhanya Arun",
    "shravani-desai": "Shravani Desai",
}


@dataclass(frozen=True)
class Exercise:
    id: str
    kind: str
    column: str


@dataclass(frozen=True)
class Topic:
    sheet: str
    comments: str
    exercises: tuple[Exercise, ...]


def select_mentee(value):
    for slug, name in MENTEES.items():
        if value.casefold() in {slug, name.casefold()}:
            return slug
    raise argparse.ArgumentTypeError(f"Unknown mentee {value!r}. Use {', '.join(MENTEES)}.")


def select_mentees(value):
    mentees = []
    for item in value.split(","):
        name = item.strip()
        if name.casefold() == "all":
            mentees.extend(MENTEES)
        else:
            mentees.append(select_mentee(name))
    return mentees


def select_topics(value):
    topics = []
    for item in value.split(","):
        item = item.strip()
        if item.casefold() == "all":
            topics.extend(range(1, 16))
            continue
        match = re.fullmatch(r"([0-9]{1,2})(?:\s*-\s*([0-9]{1,2}))?", item)
        if match:
            start = int(match[1])
            end = int(match[2] or match[1])
            if 1 <= start <= end <= 15:
                topics.extend(range(start, end + 1))
                continue
        raise argparse.ArgumentTypeError(
            f"Invalid topic selection {item!r}. Use numbers or ascending ranges from 1 to 15, or all."
        )
    return topics


def read_workbook(path, mentees, topic_numbers):
    from openpyxl import load_workbook

    workbook = load_workbook(path, read_only=True)
    try:
        roster = {
            str(row[0].value).strip(): row[0].row
            for row in workbook["Roster"].iter_rows(min_row=5, min_col=2, max_col=2)
            if row[0].value is not None
        }
        missing = [MENTEES[slug] for slug in mentees if MENTEES[slug] not in roster]
        if missing:
            raise ValueError("Names missing from workbook roster: " + ", ".join(missing))

        topics = {}
        for number in topic_numbers:
            sheets = [sheet for sheet in workbook if sheet.title.startswith(f"{number:02d} ")]
            if len(sheets) != 1:
                raise ValueError(f"Expected one worksheet for Topic {number:02d}")
            sheet = sheets[0]
            kinds, headers = sheet.iter_rows(min_row=3, max_row=4)
            exercises = []
            comments = ""
            for kind, header in zip(kinds, headers):
                value = str(header.value)
                match = re.match(rf"T{number:02d}-E\d{{2}}\b", value)
                if match:
                    exercises.append(Exercise(match[0], str(kind.value), header.column_letter))
                if value == "Trainer comments":
                    comments = header.column_letter
            if not exercises or not comments:
                raise ValueError(f"Missing exercise headers or Trainer comments in {sheet.title}")
            topics[number] = Topic(sheet.title, comments, tuple(exercises))
        return roster, topics
    finally:
        workbook.close()


def python_has_work(path):
    if path.is_dir():
        return any(python_has_work(file) for file in path.rglob("*.py"))
    if not path.is_file():
        return False
    lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    return any(line.strip() and not line.lstrip().startswith("#") for line in lines)


def check_exercise(trainer, submission, exercise, programs):
    exercise_key = exercise.id.lower().replace("-", "_")
    if not trainer.name.startswith("15-"):
        expected = programs.get(exercise_key)
        if not expected:
            raise ValueError(f"No trainer files registered for {exercise.id}")
        if not any(python_has_work(submission / path.name) for path in expected):
            return CheckResult("No submission", "Exercise files are absent or contain only the prompt.")
        return review_program_exercise(trainer, submission, exercise.id, expected)

    directory = exercise_key.upper()
    work = submission / directory
    starter = trainer / "starter" / directory
    tests = (
        file for file in work.rglob("*.py")
        if file.name.startswith("test_") or file.name.endswith("_test.py")
    )
    for file in tests:
        original = starter / file.relative_to(work)
        if python_has_work(file) and (
            not original.is_file() or file.read_bytes().replace(b"\r\n", b"\n")
            != original.read_bytes().replace(b"\r\n", b"\n")
        ):
            return review_test_exercise(starter, trainer / "buggy" / directory, work, verbose=False)
    return CheckResult("No submission", "Waiting for mentee-written tests.")


def rating_guidance(result):
    if result.status in {"Failed checks", "Incomplete files"}:
        return 2, "Confirm that the attempt is incomplete."
    if result.status == "Passed checks":
        return "", "Consider 3, 4, or 5 after checking help received, code quality, and tests."
    if result.status == "Check error":
        return "", "Resolve the check error or assess the exercise manually."
    return "", "Enter 1 only if assessed as not started. Otherwise leave blank."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", "--topics", action="extend", type=select_topics,
                        metavar="SELECTION", help="topic numbers, ranges, or all (e.g. 1,3-5)")
    parser.add_argument("--user", "--users", action="extend", type=select_mentees,
                        metavar="SELECTION", help="comma-separated mentee names or folders, or all")
    parser.add_argument("--training-dir", type=Path, default=ROOT.parent / "python training",
                        help="location of the original trainer materials")
    parser.add_argument("--workbook", type=Path, help="read-only rubric workbook locator")
    parser.add_argument("--submissions-dir", type=Path, default=ROOT / "submissions",
                        help="submission directory from the checkout to review")
    parser.add_argument("--output", type=Path, help="new CSV path under review-results by default")
    args = parser.parse_args()

    mentees = list(dict.fromkeys(args.user or MENTEES))
    numbers = sorted(set(args.topic or range(1, 16)))
    workbook_path = args.workbook or args.training_dir / "python-topic-evaluation.xlsx"
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    output = args.output or ROOT / "review-results" / f"evaluation-{timestamp}.csv"
    if output.suffix.lower() != ".csv":
        parser.error("--output must end in .csv")
    if output.exists():
        parser.error(f"Report already exists: {output}")
    for slug in mentees:
        if not (args.submissions_dir / slug).is_dir():
            parser.error(f"Missing mentee directory: {args.submissions_dir / slug}")

    counts = Counter()
    rows = []
    try:
        roster, topics = read_workbook(workbook_path, mentees, numbers)
        for number, topic in topics.items():
            public_topic, = (ROOT / "exercises").glob(f"{number:02d}-*")
            trainer = args.training_dir / public_topic.name
            programs = defaultdict(list)
            if number < 15:
                for path in expected_programs(trainer, f"{number:02d}"):
                    match = EXERCISE_MODULE.match(path.name)
                    key = match.group(1).lower() if match else "t14_e12"
                    programs[key].append(path)

            for slug in mentees:
                print(f"{number:02d} {MENTEES[slug]}", flush=True)
                submission = args.submissions_dir / slug / public_topic.name
                row_number = roster[MENTEES[slug]]
                for exercise in topic.exercises:
                    try:
                        result = check_exercise(trainer, submission, exercise, programs)
                    except (OSError, ValueError, SyntaxError, ElementTree.ParseError,
                            subprocess.TimeoutExpired) as error:
                        result = CheckResult("Check error", str(error))
                    suggested, guidance = rating_guidance(result)
                    counts[result.status] += 1
                    rows.append([
                        MENTEES[slug], f"{number:02d}", exercise.id, exercise.kind,
                        topic.sheet, f"{exercise.column}{row_number}", f"{topic.comments}{row_number}",
                        result.status, suggested, "", guidance, result.evidence,
                    ])
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("x", encoding="utf-8-sig", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Mentee", "Topic", "Exercise", "Type", "Workbook sheet", "Rating cell",
                "Trainer comments cell", "Check", "Suggested rating", "Your rating",
                "Rating guidance", "Test evidence",
            ])
            writer.writerows(rows)
    except (OSError, ValueError, KeyError, ImportError) as error:
        print(f"Report error: {error}", file=sys.stderr)
        return 2

    print(f"Report written to {output.resolve()}")
    print(", ".join(f"{status} ({count})" for status, count in counts.items()))
    return 1 if counts["Check error"] else 0


if __name__ == "__main__":
    sys.exit(main())
