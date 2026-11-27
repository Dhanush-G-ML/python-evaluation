"""Run the trainer's existing checks on a checked-out topic submission."""

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from xml.etree import ElementTree


IGNORE_GENERATED = shutil.ignore_patterns(
    "__pycache__", ".venv", ".pytest_cache", ".coverage*", "htmlcov", "output"
)
COVERAGE_MODULES = {
    "T15_E10": "loyalty",
    "T15_E11": "cart",
    "T15_E12": "inventory_reader",
}


def run_pytest(directory, *options, quiet=False):
    command = [
        sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
        f"--basetemp={directory / 'pytest-tmp'}", *options
    ]
    env = dict(os.environ, PYTEST_ADDOPTS="", PYTHONDONTWRITEBYTECODE="1", PYTHONUTF8="1")
    return subprocess.run(
        command,
        cwd=directory,
        env=env,
        timeout=180,
        capture_output=quiet,
        encoding="utf-8" if quiet else None,
        errors="replace" if quiet else None,
    )


def review_programs(trainer_topic, submission, topic_number):
    # The reference directory provides the expected filenames. Pytest receives only
    # submitted implementations, the trainer's tests, and the original data.
    reference = trainer_topic / "solutions"
    if not reference.is_dir() or not (trainer_topic / "tests").is_dir():
        raise ValueError(f"Expected the original trainer topic at {trainer_topic}")
    expected = sorted(
        path for path in reference.iterdir()
        if re.match(rf"^T{topic_number}_E\d{{2}}(?:_|\.|$)", path.name, re.IGNORECASE)
    )
    if topic_number == "14":
        expected.append(reference / "shop")
    if not expected:
        raise ValueError(f"Could not find expected exercise names in {reference}")

    submitted = {path.name: path for path in submission.iterdir()}
    missing = [
        path.name for path in expected
        if path.name not in submitted or submitted[path.name].is_dir() != path.is_dir()
    ]
    if missing:
        print("Complete-topic check needs these files or folders:")
        for name in missing:
            print(f"  {name}")
        return 1

    with tempfile.TemporaryDirectory(prefix="python-review-") as temporary:
        stage = Path(temporary)
        shutil.copytree(submission, stage / "solutions", ignore=IGNORE_GENERATED)
        shutil.copytree(trainer_topic / "tests", stage / "tests", ignore=IGNORE_GENERATED)
        for name in ("data", "examples"):
            if (trainer_topic / name).is_dir():
                shutil.copytree(trainer_topic / name, stage / name, ignore=IGNORE_GENERATED)
        if topic_number == "14" and os.name == "nt":
            logging_tests = stage / "tests" / "test_t14_logging.py"
            checks = logging_tests.read_text(encoding="utf-8")
            # The sample uses POSIX separators. The trainer's JSON formatter
            # calls str(Path(...)), which produces native separators on Windows.
            portable = checks.replace(
                'assert records[1]["file"] == "invoices/a-17.pdf"',
                'assert Path(records[1]["file"]).as_posix() == "invoices/a-17.pdf"',
            )
            if portable != checks:
                logging_tests.write_text(portable, encoding="utf-8")
        return run_pytest(stage, "-vv", "tests").returncode


def stage_test_exercise(work, submission, starter):
    shutil.copytree(submission, work, ignore=IGNORE_GENERATED)
    for original in sorted(starter.iterdir()):
        if original.name.startswith("test_") or original.name == "extra_tests.py":
            continue
        if not original.is_file():
            continue
        destination = work / original.name
        if destination.exists() and (
            not destination.is_file()
            or destination.read_bytes().replace(b"\r\n", b"\n")
            != original.read_bytes().replace(b"\r\n", b"\n")
        ):
            raise ValueError(f"Starter file changed: {submission / original.name}")
        shutil.copy2(original, destination)


def test_cases(report):
    if not report.is_file():
        return []
    return list(ElementTree.parse(report).iter("testcase"))


def review_test_exercise(starter, variants, submission):
    exercise = starter.name
    print(f"\n{exercise}", flush=True)
    with tempfile.TemporaryDirectory(prefix="pytest-review-") as temporary:
        stage = Path(temporary)
        report = stage / "result.xml"
        report_option = f"--junitxml={report}"
        original_work = stage / "original"
        stage_test_exercise(original_work, submission, starter)
        options = []
        if module := COVERAGE_MODULES.get(exercise):
            options = [f"--cov={module}", "--cov-report=term-missing", "--cov-fail-under=90"]
        baseline = run_pytest(original_work, report_option, *options)
        if baseline.returncode or not any(
            case.find("skipped") is None for case in test_cases(report)
        ):
            print("Baseline check failed. Run against the starter until at least one test passes.")
            return False

        variant_dirs = sorted(path for path in variants.iterdir() if path.is_dir())
        if not variant_dirs:
            raise ValueError(f"No trainer variants found in {variants}")
        caught = 0
        for variant in variant_dirs:
            with tempfile.TemporaryDirectory(dir=stage) as variant_temp:
                work = Path(variant_temp) / "submission"
                stage_test_exercise(work, submission, starter)
                for replacement in variant.iterdir():
                    if replacement.is_file() and replacement.suffix == ".py":
                        shutil.copy2(replacement, work / replacement.name)
                report.unlink(missing_ok=True)
                result = run_pytest(work, report_option, quiet=True)
                if result.returncode == 1 and any(
                    case.find("failure") is not None or case.find("error") is not None
                    for case in test_cases(report)
                ):
                    caught += 1
                    print(f"  Caught: {variant.name}")
                elif result.returncode == 0:
                    print(f"  Missed: {variant.name}")
                else:
                    print(f"  Review error: {variant.name} (pytest exit {result.returncode})")
                    print(result.stdout + result.stderr)
        print(f"Variants caught: {caught}/{len(variant_dirs)}")
        return caught == len(variant_dirs)


def review_tests(trainer_topic, submission, exercise_number):
    starter = trainer_topic / "starter"
    buggy = trainer_topic / "buggy"
    if not starter.is_dir() or not buggy.is_dir():
        raise ValueError(f"Expected the original trainer topic at {trainer_topic}")
    if exercise_number is None:
        exercises = sorted(
            path.name for path in starter.iterdir()
            if path.is_dir() and (submission / path.name).is_dir()
        )
    else:
        name = f"T15_E{exercise_number:02d}"
        if not (submission / name).is_dir():
            raise ValueError(f"Missing submission folder: {submission / name}")
        exercises = [name]
    if not exercises:
        raise ValueError(f"No Topic 15 exercise submissions found in {submission}")
    results = [
        review_test_exercise(starter / name, buggy / name, submission / name)
        for name in exercises
    ]
    return 0 if all(results) else 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--training-dir", type=Path, required=True,
                        help="path to the original trainer materials")
    parser.add_argument("--submission", type=Path, required=True,
                        help="path to a mentee's checked-out topic directory")
    parser.add_argument("--exercise", type=int, choices=range(1, 13),
                        help="check one Topic 15 exercise by number")
    args = parser.parse_args()

    submission = args.submission.resolve()
    trainer_topic = args.training_dir.resolve() / submission.name
    topic_number = submission.name[:2]
    if not submission.is_dir() or not re.fullmatch(r"(0[1-9]|1[0-5])-[a-z-]+", submission.name):
        parser.error("--submission must point to an existing topic directory")
    if args.exercise is not None and topic_number != "15":
        parser.error("--exercise applies to Topic 15")

    print(f"Reviewing {submission}", flush=True)
    try:
        if topic_number == "15":
            return review_tests(trainer_topic, submission, args.exercise)
        return review_programs(trainer_topic, submission, topic_number)
    except (OSError, ValueError, ElementTree.ParseError, subprocess.TimeoutExpired) as error:
        print(f"Review error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
