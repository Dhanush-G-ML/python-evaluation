# Mentor Review Guide

Review the pull request against the assigned exercise IDs. Enter ratings and feedback in the yellow input cells of the matching topic sheet in the manager's evaluation workbook.

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
2. Fetch the submission and create a detached worktree at the commit you intend to review. In the following PowerShell example, replace the branch name and commit SHA with the actual values.

   ```powershell
   git fetch origin submission/alex/01
   git worktree add --detach ../python-review-alex <commit-sha>
   ```

3. From the trainer's checkout of this repository, install the review dependencies into a Python 3.12 environment and run the checker. Use an isolated environment for running submissions because pytest executes the submitted Python code. Point `--training-dir` at the original trainer materials.

   ```powershell
   python -m pip install -r requirements-review.txt
   python tools/review_submission.py --training-dir "../python training" --submission "../python-review-alex/submissions/alex/01-lists-dicts-strings"
   ```

   Topics 01–14 use the trainer's complete-topic pytest suites. The checker lists missing files before running and prints each test result by name. For a smaller assignment in those topics, review each assigned exercise's acceptance checklist and run its sample inputs and relevant boundary cases directly. On Windows, the checker accepts either path separator for the T14-E08 JSON example.

   For Topic 15, change the submission path to `15-pytest-basics` and add `--exercise 1` to check just T15-E01. By default, the checker reviews each submitted Topic 15 exercise. It runs the tests against the original starter implementation, checks coverage for T15-E10 through T15-E12, and reports which trainer variants the tests catch. Compare assignment-specific fixture, marker and assertion requirements with the exercise checklist.

4. Read the code and review behavior, including edge cases, against the exercise acceptance criteria. Record concrete evidence from the runs and code review alongside the manager's ratings. Keep scores and private notes in the evaluation workbook. Use the PR to give feedback on the code.

The checker stages the tests and submission in temporary folders. Keep the trainer materials outside this repository and use the original folder as the source for evaluation.
