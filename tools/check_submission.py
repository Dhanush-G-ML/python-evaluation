"""Check the contents of a mentee pull request without executing its code."""

import argparse
from pathlib import PurePosixPath
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

    base = git("rev-parse", "--verify", "--end-of-options", f"{args.base}^{{commit}}").decode().strip()
    head = git("rev-parse", "--verify", "--end-of-options", f"{args.head}^{{commit}}").decode().strip()
    changes = git("diff", "--name-only", "--no-renames", "-z", f"{base}...{head}", "--")
    files = changes.decode("utf-8").split("\0")[:-1]
    if not files:
        parser.error("Add your exercise work before opening a pull request.")

    base_files = git("ls-tree", "-r", "--name-only", "-z", f"{base}:submissions")
    known_topics = {
        path.parts[:2]
        for path in map(PurePosixPath, base_files.decode("utf-8").split("\0")[:-1])
        if len(path.parts) >= 3
    }
    topics = {
        path.parts[1:3]
        for path in map(PurePosixPath, files)
        if len(path.parts) >= 4
        and path.parts[0] == "submissions"
        and path.parts[1:3] in known_topics
    }
    if not topics and args.author.casefold() == args.owner.casefold():
        print("Repository owner maintenance PR.")
        return 0
    if len(topics) != 1:
        parser.error("Change files in exactly one existing submission topic folder.")

    mentee, topic = topics.pop()
    directory = f"submissions/{mentee}/{topic}/"
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
    print(f"Submission checks passed for {directory} on branch {args.branch!r}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
