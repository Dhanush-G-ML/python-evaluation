"""Check the contents of a mentee pull request without executing its code."""

import argparse
import re
import subprocess
import sys


def git(*args):
    return subprocess.check_output(["git", *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--branch", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--owner", required=True)
    args = parser.parse_args()

    if not args.branch.startswith("submission/") and args.author.casefold() == args.owner.casefold():
        print("Repository owner maintenance PR.")
        return 0

    branch = re.fullmatch(r"submission/([a-z0-9-]+)/(0[1-9]|1[0-5])", args.branch)
    if not branch:
        parser.error("Use submission/<your-folder>/<two-digit-topic> for your branch name.")
    mentee, topic = branch.groups()

    base = git("rev-parse", "--verify", "--end-of-options", f"{args.base}^{{commit}}").decode().strip()
    head = git("rev-parse", "--verify", "--end-of-options", f"{args.head}^{{commit}}").decode().strip()
    mentees = git("ls-tree", "-d", "--name-only", f"{base}:submissions").decode().splitlines()
    if mentee not in mentees:
        parser.error(f"Unknown mentee folder {mentee!r}.")
    folders = git("ls-tree", "-d", "--name-only", f"{base}:submissions/{mentee}").decode().splitlines()
    topics = [folder for folder in folders if folder.startswith(f"{topic}-")]
    if len(topics) != 1:
        parser.error(f"No topic {topic} submission folder exists for {mentee}.")
    directory = f"submissions/{mentee}/{topics[0]}/"

    changes = git("diff", "--name-only", "--no-renames", "-z", f"{base}...{head}", "--")
    files = changes.decode("utf-8").split("\0")[:-1]
    if not files:
        parser.error("Add your exercise work before opening a pull request.")
    outside = [file for file in files if not file.startswith(directory)]
    if outside:
        for file in outside:
            print(f"Outside your topic folder: {file!r}", file=sys.stderr)
        parser.error(f"Keep this pull request within {directory}")

    python_files = git("diff", "--name-only", "--no-renames", "--diff-filter=ACMT",
                       "-z", f"{base}...{head}", "--", "*.py")
    failed = False
    for file in python_files.decode("utf-8").split("\0")[:-1]:
        try:
            compile(git("show", f"{head}:{file}"), file, "exec")
        except SyntaxError as error:
            print(f"{error.filename}:{error.lineno}: {error.msg}", file=sys.stderr)
            failed = True
    if failed:
        return 1
    print(f"Submission checks passed for {directory} ({len(files)} changed files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
