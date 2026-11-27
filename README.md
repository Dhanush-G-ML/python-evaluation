# Python Training Submissions

Use this repository to practice Python, Git and GitHub together. For each assigned topic, you'll create a branch, commit your work, open a pull request and respond to review feedback. The exercises include sample output and acceptance checklists so you can verify your work before submitting it.

## Exercise bank

| Topic | Exercises |
| --- | ---: |
| [01 Lists, dicts, sets, tuples and strings](exercises/01-lists-dicts-strings/exercises.md) | 11 |
| [02 Basic programs](exercises/02-basic-programs/exercises.md) | 10 |
| [03 File handling](exercises/03-file-handling/exercises.md) | 10 |
| [04 Exception handling](exercises/04-exception-handling/exercises.md) | 10 |
| [05 JSON](exercises/05-json/exercises.md) | 10 |
| [06 Regular expressions](exercises/06-regex/exercises.md) | 10 |
| [07 Object-oriented programming](exercises/07-oop/exercises.md) | 10 |
| [08 Decorators](exercises/08-decorators/exercises.md) | 10 |
| [09 Recursion](exercises/09-recursion/exercises.md) | 11 |
| [10 Design patterns](exercises/10-design-patterns/exercises.md) ([worked examples](exercises/10-design-patterns/worked-examples.md)) | 10 |
| [11 Data structures](exercises/11-data-structures/exercises.md) | 12 |
| [12 Algorithms](exercises/12-algorithms/exercises.md) | 12 |
| [13 Complex programs](exercises/13-complex-programs/exercises.md) | 10 |
| [14 Logging](exercises/14-logging/exercises.md) | 12 |
| [15 Pytest basics](exercises/15-pytest-basics/exercises.md) | 12 |

## Submit your work

**Git** tracks changes on your computer. A **branch** gives you a place to work on one topic, and a **commit** records a group of related changes. **GitHub** hosts the shared repository. A **pull request (PR)** lets reviewers see your changes and discuss them before they go into `main`.

### 1. Clone the repository

You'll need Git, Python 3.12 and a GitHub account with write access to this repository. On the repository's GitHub page, select **Code** and copy the **HTTPS** URL. Replace `<repo-url>` with that URL. Use your name and the commit email associated with your GitHub account for the other placeholders.

```powershell
git clone "<repo-url>"
cd python-evaluation
git config --local user.name "<your-name>"
git config --local user.email "<your-commit-email>"
```

Cloning downloads a local copy. Git calls the GitHub repository you cloned from `origin`. The `--local` settings give your commits in this repository the right name and email.

### 2. Start a branch for your topic

Replace each angle-bracket placeholder with your own value.

- `<your-folder>` is your exact folder name from the [submission folder list](submissions/README.md).
- `<topic-folder>` is the full folder name of your assigned topic in the exercise bank.
- `<topic-number>` is the two-digit prefix of that topic folder.

```powershell
git switch main
git pull --ff-only
git switch -c "submission/<your-folder>/<topic-number>"
```

`git pull --ff-only` brings your local `main` up to date if Git can advance it without a merge. `git switch -c` creates the topic branch and switches to it. Open `submissions/<your-folder>/<topic-folder>/` and add code to the question files for your assigned exercises. Run them against the samples and acceptance checklist in the exercise instructions. Keep demonstrations under `if __name__ == "__main__":` so the reviewer can import your functions or classes.

### 3. Review, commit and push your changes

From the repo root, run these commands on your submission branch.

```powershell
git status
git diff
git add -- "submissions/<your-folder>/<topic-folder>/"
git diff --staged
git commit -m "Submit Topic <topic-number> exercises"
git push -u origin "submission/<your-folder>/<topic-number>"
```

Use `git status` to confirm the branch and see the files you changed. `git diff` shows unstaged edits to tracked files. `git add` selects files for the next commit, and `git diff --staged` lets you review exactly what you're about to commit. The first push publishes your branch on GitHub and connects it to your local branch so later pushes can use `git push`.

### 4. Open and review your pull request on GitHub

1. Open the repository on GitHub and choose **Compare & pull request** for the branch you pushed.
2. Set the **base** branch to `main` and the **compare** branch to `submission/<your-folder>/<topic-number>`. Check that the diff contains files from your own topic folder.
3. Use `<your-name> | Topic <topic-number>` as the title. Fill in the PR template with your exercise IDs, commands and results, and any references or help you used. Select **Create pull request** and request your mentor's review.
4. Open the **Checks** tab and look for **Submission checks**. It verifies the branch name, the changed file paths and Python syntax. If it fails, open the check log to find the exact problem.

`main` requires passing checks, resolved review threads and two approvals, including one from the repository owner. See the [pull request rules](CONTRIBUTING.md).

### 5. Respond to feedback and start the next topic

Make requested edits on the same branch, check your diff, stage the files and make a new commit. Run `git push` to update the existing PR. Reply to review comments so reviewers can see how you addressed them.

After your PR merges, switch to `main` and run `git pull --ff-only` before starting the next topic branch.

### File names and local checks

- **Topics 01–10 and 14.** Work in the file named after the exercise, using the `T<topic-number>_E<exercise-number>.py` format. Topic 14 exercise 12 also uses the `shop/` package next to `T14_E12.py`. To run an exercise that expects `data/`, start from the repo root and use the exact Python filename (including `.py`) for `<exercise-file>`.

  ```powershell
  cd "exercises/<topic-folder>"
  python "../../submissions/<your-folder>/<topic-folder>/<exercise-file>"
  ```

- **Topics 11–12.** Use the exact filename listed under each exercise heading.
- **Topic 13.** The named packages have a question in `__main__.py`. Add the modules requested by the exercise and run `python -m <package_name>` from your topic submission folder. Use the sample data path given at the top of the topic.
- **Topic 15.** Write your tests in the question files under your `T15_E##/` folders. For local testing, copy the supplied implementation and any data files from the matching shared `starter/T15_E##/` folder into your exercise directory. When an exercise asks you to fix the supplied starter tests, read them in the shared folder and bring the relevant code into your question file. Run `python -m pytest` from your exercise directory. Commit your test files and any test configuration you wrote. Install pytest and pytest-cov with `python -m pip install -r requirements-review.txt` from the repository root first.

Treat `exercises/` as shared reference material and keep your pull request scoped to your submission folder.

Mentors can use the [review guide](REVIEW.md) to check a specific submission commit.
