"""Make a progress CSV from the files in the shared repository."""

import argparse
import csv
from pathlib import Path
import re

from report_evaluation import (
    MENTEES,
    ROOT,
    has_written_tests,
    python_has_work,
    select_mentees,
    select_topics,
)


def question_files(topic):
    number = int(topic.name[:2])
    text = (topic / "exercises.md").read_text(encoding="utf-8")
    blocks = re.split(r"(?m)^## (?=T\d{2}-E\d{2}\b)", text)[1:]
    for block in blocks:
        exercise = block[:7]
        stem = exercise.replace("-", "_")
        if number in (11, 12):
            name = re.search(r"Submit as `([^`]+)`", block)[1]
        elif number == 13:
            name = re.search(r"\*\*Package:\*\* `([^`]+)`", block)[1]
        elif number == 15:
            name = stem
        else:
            name = f"{stem}.py"
        yield exercise, name


def has_submission(topic, folder, exercise, name):
    path = folder / name
    if exercise == "T14-E12":
        return python_has_work(path) or python_has_work(folder / "shop")
    if exercise.startswith("T15-"):
        return has_written_tests(path, topic / "starter" / name)
    return python_has_work(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", action="extend", type=select_topics)
    parser.add_argument("--user", action="extend", type=select_mentees)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    users = dict.fromkeys(args.user or MENTEES)
    topics = sorted(set(args.topic or range(1, 16)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8-sig", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["Mentee", "Topic", "Exercise", "Progress"])
        for number in topics:
            topic, = (ROOT / "exercises").glob(f"{number:02d}-*")
            exercises = list(question_files(topic))
            for user in users:
                folder = ROOT / "submissions" / user / topic.name
                for exercise, name in exercises:
                    status = "Code present" if has_submission(topic, folder, exercise, name) else "Awaiting code"
                    writer.writerow([MENTEES[user], f"{number:02d}", exercise, status])
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
