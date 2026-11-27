"""Run the trainer's existing checks on a checked-out topic submission."""

import argparse
import ast
from dataclasses import dataclass
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
EXERCISE_MODULE = re.compile(r"^(t\d{2}_e\d{2})(?:_|\.|$)", re.IGNORECASE)


@dataclass(frozen=True)
class CheckResult:
    status: str
    evidence: str


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


def expected_programs(trainer_topic, topic_number):
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
    return expected


def stage_program_checks(trainer_topic, stage):
    shutil.copytree(trainer_topic / "tests", stage / "tests", ignore=IGNORE_GENERATED)
    for name in ("data", "examples"):
        if (trainer_topic / name).is_dir():
            shutil.copytree(trainer_topic / name, stage / name, ignore=IGNORE_GENERATED)
    if trainer_topic.name.startswith("14-") and os.name == "nt":
        logging_tests = stage / "tests" / "test_t14_logging.py"
        checks = logging_tests.read_text(encoding="utf-8")
        # str(Path(...)) produces native separators on Windows.
        portable = checks.replace(
            'assert records[1]["file"] == "invoices/a-17.pdf"',
            'assert Path(records[1]["file"]).as_posix() == "invoices/a-17.pdf"',
        )
        if portable != checks:
            logging_tests.write_text(portable, encoding="utf-8")


def review_programs(trainer_topic, submission, topic_number):
    expected = expected_programs(trainer_topic, topic_number)
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
        stage_program_checks(trainer_topic, stage)
        return run_pytest(stage, "-vv", "tests").returncode


def imports_other_exercise(module, exercise):
    match = EXERCISE_MODULE.match(module)
    return match is not None and match.group(1).lower() != exercise


def scope_test_imports(test_file, exercise):
    tree = ast.parse(test_file.read_text(encoding="utf-8"))
    scoped = []
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and imports_other_exercise(node.module or "", exercise):
            continue
        if isinstance(node, ast.Import):
            node.names = [
                name for name in node.names if not imports_other_exercise(name.name, exercise)
            ]
            if not node.names:
                continue
        if isinstance(node, ast.FunctionDef) and node.name == "test_t12_e02_to_e04_sorts_match_sorted":
            # Keep the assertions for the selected sort and the shared no-mutation assertion.
            foreign_aliases = {"e02", "e03", "e04"} - {exercise[-3:]}
            node.body = [
                statement for statement in node.body
                if not isinstance(statement, ast.Assert) or not any(
                    isinstance(item, ast.Name) and item.id in foreign_aliases
                    for item in ast.walk(statement)
                )
            ]
        scoped.append(node)
    tree.body = scoped
    test_file.write_text(ast.unparse(tree) + "\n", encoding="utf-8")


def review_program_exercise(trainer_topic, submission, exercise_id, expected):
    exercise = exercise_id.lower().replace("-", "_")
    paths = {path.name: path for path in submission.iterdir()} if submission.is_dir() else {}
    present = [path for path in expected if path.name in paths]
    if not present:
        return CheckResult("No submission", "Expected " + ", ".join(path.name for path in expected))
    missing = [
        path.name for path in expected
        if path.name not in paths or paths[path.name].is_dir() != path.is_dir()
    ]
    if missing:
        return CheckResult("Incomplete files", "Missing " + ", ".join(missing))

    with tempfile.TemporaryDirectory(prefix="python-exercise-") as temporary:
        stage = Path(temporary)
        solutions = stage / "solutions"
        solutions.mkdir()
        for path in present:
            source = paths[path.name]
            if path.is_dir():
                shutil.copytree(source, solutions / path.name, ignore=IGNORE_GENERATED)
            else:
                shutil.copy2(source, solutions / path.name)
        stage_program_checks(trainer_topic, stage)
        for test_file in (stage / "tests").glob("test_*.py"):
            scope_test_imports(test_file, exercise)
        selector = f"test_{exercise[-3:]} or {exercise}"
        if exercise in {"t12_e02", "t12_e03", "t12_e04"}:
            selector += " or test_t12_e02_to_e04_sorts_match_sorted"
        report = stage / "result.xml"
        result = run_pytest(stage, "tests", "-k", selector, f"--junitxml={report}", quiet=True)
        cases = test_cases(report)
        if result.returncode == 0 and any(case.find("skipped") is None for case in cases):
            return CheckResult("Passed checks", summarize_pytest(result, cases))
        if result.returncode == 1 and cases:
            return CheckResult("Failed checks", summarize_pytest(result, cases))
        return CheckResult("Check error", summarize_pytest(result, cases))


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


def summarize_pytest(result, cases):
    lines = result.stdout.splitlines() + result.stderr.splitlines()
    if cases:
        failed = [
            case.get("name", "") for case in cases
            if case.find("failure") is not None or case.find("error") is not None
        ]
        skipped = sum(case.find("skipped") is not None for case in cases)
        passed = len(cases) - len(failed) - skipped
        summary = f"{passed} passed, {len(failed)} failed or errored, {skipped} skipped/xfailed"
        if failed:
            summary += ". " + ", ".join(failed[:3])
        if result.returncode in (0, 1):
            coverage = next((line.strip() for line in lines if "Total coverage:" in line), "")
            return ". ".join(part for part in (summary, coverage) if part)
    detail = next(
        (line.strip() for line in reversed(lines)
         if "Error:" in line or line.startswith(("ERROR ", "ERROR:"))),
        "",
    )
    return f"pytest exit {result.returncode}. {detail}".rstrip(". ")


def review_test_exercise(starter, variants, submission, *, verbose=True):
    exercise = starter.name
    if verbose:
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
        baseline = run_pytest(original_work, report_option, *options, quiet=True)
        cases = test_cases(report)
        baseline_evidence = summarize_pytest(baseline, cases)
        if verbose:
            print(baseline.stdout + baseline.stderr, end="")
        if baseline.returncode or not any(case.find("skipped") is None for case in cases):
            status = "Failed checks" if baseline.returncode in (0, 1, 5) else "Check error"
            return CheckResult(status, "Starter run: " + baseline_evidence)

        variant_dirs = sorted(path for path in variants.iterdir() if path.is_dir())
        if not variant_dirs:
            raise ValueError(f"No trainer variants found in {variants}")
        missed = []
        errors = []
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
                    if verbose:
                        print(f"  Caught: {variant.name}")
                elif result.returncode == 0:
                    missed.append(variant.name)
                    if verbose:
                        print(f"  Missed: {variant.name}")
                else:
                    errors.append(variant.name)
                    if verbose:
                        print(f"  Review error: {variant.name} (pytest exit {result.returncode})")
                        print(result.stdout + result.stderr)
        caught = len(variant_dirs) - len(missed) - len(errors)
        summary = f"Variants caught: {caught}/{len(variant_dirs)}"
        if verbose:
            print(summary)
        evidence = f"Starter run: {baseline_evidence}. {summary}"
        if missed:
            evidence += ". Missed: " + ", ".join(missed)
        if errors:
            evidence += ". Variant errors: " + ", ".join(errors)
            return CheckResult("Check error", evidence)
        return CheckResult("Failed checks" if missed else "Passed checks", evidence)


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
    return 0 if all(result.status == "Passed checks" for result in results) else 1


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
