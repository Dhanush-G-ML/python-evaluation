# Mentor Review Guide

Run the evaluation report to get the test evidence and the exact worksheet and cell for each exercise rating. The report reads the manager's workbook and writes a CSV under `review-results/`. Enter the confirmed ratings and feedback in Excel yourself.

## Generate a report

From the trainer's checkout, install the review dependencies in a Python 3.12 environment. Run submissions in an isolated environment because pytest executes submitted Python code.

```powershell
python -m pip install -r requirements-review.txt
python tools/report_evaluation.py --topic "1,2"
python tools/report_evaluation.py --topic "1-3" --user all
python tools/report_evaluation.py --topic "1,3-5" --user "Sahana,Dhanya"
python tools/report_evaluation.py --topic all --user "rishitaa,SHRAVANI"
```

Topic ranges include both endpoints. Select mentees by first name in any letter case. Quote comma-separated selections in PowerShell. Both filters can be repeated and default to `all` when omitted. The report uses the sibling `python training` folder by default. Use `--training-dir` or `--workbook` to point at a different location.

The CSV includes **Workbook sheet**, **Rating cell**, **Trainer comments cell**, **Check**, **Suggested rating**, **Your rating**, and the test evidence. Question-only files appear as **No submission**, with a blank rating. Failed checks or incomplete files suggest a provisional **2**. For passing checks, use the rubric and the PR review to choose a rating. Review individual errors before entering any value.

## GitHub Actions

The **Pull request validation** workflow checks PR scope and Python syntax. The **Submission progress** workflow creates a `submission-progress` CSV artifact after a push or merge to `main`. For a filtered progress report, open **Actions**, select **Submission progress**, choose **Run workflow**, and enter topics and first names. Download the CSV from the run's **Artifacts** section.

On the sample branch `submission/sample-user/01`, **Submission checks** also runs a public pytest test for the greeting after the syntax check passes.

The progress CSV shows which exercises have code. Use the local evaluation command for private trainer tests and Excel rating evidence. GitHub artifacts are accessible to people with read access to this repo.

The `.github/main-ruleset.json` file can be imported in **Settings → Rules → Rulesets** on a plan that supports rulesets for this repository. Once active, it requires a passing **Submission checks** result from GitHub Actions, resolved review threads, and two approvals for every PR into `main`. One approval must come from `@Dhanush-G-ML`, the code owner, and the other from a different reviewer with write access. It also blocks force pushes and deletion of `main`. The owner-authored sample PR cannot satisfy the owner-approval requirement because GitHub prevents authors from approving their own PRs.

## Apply the workbook rubric

| Rating | Evidence |
| --- | --- |
| 1 | Exercise has yet to be started |
| 2 | Attempted and incomplete |
| 3 | Meets the specification with help |
| 4 | Meets the specification independently |
| 5 | Meets the specification with clean code and tests, or goes beyond the specification |

Leave the rating blank for an unassessed exercise. Use the exercise ID to find its column and use **Trainer comments** for the PR number, commit SHA, test evidence and support needed. Passing tests are one form of evidence. Use the code review and a brief walkthrough to assess independence and the quality of the work.

The workbook calculates core and challenge averages separately. With its default settings, a core average of at least 3 passes the topic and every core exercise needs a rating of at least 3 for the topic to count as complete in **Summary**. For the interview-style assessment, use the prompts in **Interview Skills** and enter ratings for skills assessed. **Interview Results** calculates the results and has its own trainer comments field.

## Review a submission

1. Check the pull request's changed files and note the assigned IDs and head commit. The branch and pull request are visible to others who have access to the shared repository.
2. For a PR that is still open, fetch its branch and create a detached worktree at the head SHA.

   ```powershell
   git fetch origin submission/dhanya-arun/01
   git worktree add --detach ../python-review-dhanya FETCH_HEAD
   ```

3. From the trainer's checkout, run the report against that worktree. The report checks each submitted exercise independently, so a partial PR produces results for the work it contains.

   ```powershell
   python tools/report_evaluation.py --topic 01 --user Dhanya --submissions-dir ../python-review-dhanya/submissions
   ```

   For Topic 15, the report runs the mentee's tests against the original starter implementation, checks coverage for T15-E10 through T15-E12, and reports which trainer variants the tests catch. Compare assignment-specific fixture, marker and assertion requirements with the exercise checklist.

4. Read the code and review behavior, including edge cases, against the exercise acceptance criteria. Record concrete evidence from the runs and code review alongside the manager's ratings. Keep scores and private notes in the evaluation workbook. Use the PR to give feedback on the code.

The checker stages the tests and submission in temporary folders. Keep the trainer materials outside this repository and use the original folder as the source for evaluation. For full pytest output on a completed topic, run `python tools/review_submission.py --help`.
