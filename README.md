# Python Training Submissions

Use this repository to submit your assigned Python exercises for mentor review. Each topic includes its problem statements, sample output and acceptance checklists. Start with the exercise IDs your mentor assigns.

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

1. Clone the repo and find your [submission folder](submissions/README.md). Start one branch per topic from `main`. For example, Dhanya can run `git switch -c submission/dhanya-arun/01` for Topic 01.
2. Open the assigned topic under your folder and add your code to its question-only files. For Topic 01, Dhanya works under `submissions/dhanya-arun/01-lists-dicts-strings/`.
3. Use Python 3.12 and check your work against the samples and acceptance checklist. Keep demonstrations under `if __name__ == "__main__":` so the reviewer can import the functions or classes.
4. Commit your own topic folder and push the branch. For this example:

   ```powershell
   git add -- submissions/dhanya-arun/01-lists-dicts-strings/
   git commit -m "Submit Topic 01 exercises"
   git push -u origin submission/dhanya-arun/01
   ```

5. On GitHub, select **Compare & pull request** for the branch you just pushed. Check that the base is `main` and the compare branch is yours. Give the PR a title such as `Dhanya Arun | Topic 01`, fill in the exercise IDs and verification commands, and select **Create pull request**. Request your mentor's review. Push any requested changes to the same branch to update the PR.

### File names and local checks

- **Topics 01–10 and 14.** Work in the file named after the exercise, such as `T01_E01.py`. Topic 14 exercise 12 also uses the `shop/` package next to `T14_E12.py`. To run an exercise that expects `data/`, change into the shared exercise folder first. For example, from the repo root run `cd exercises/03-file-handling` then `python ../../submissions/dhanya-arun/03-file-handling/T03_E01.py`.
- **Topics 11–12.** Use the exact filename listed under each exercise heading.
- **Topic 13.** The named packages have a question in `__main__.py`. Add the modules requested by the exercise and run `python -m <package_name>` from your topic submission folder. Use the sample data path given at the top of the topic.
- **Topic 15.** Write your tests in the question files under your `T15_E##/` folders. For local testing, copy the supplied implementation and any data files from the matching shared `starter/T15_E##/` folder into your exercise directory. When an exercise asks you to fix the supplied starter tests, read them in the shared folder and bring the relevant code into your question file. Run `python -m pytest` from your exercise directory. Commit your test files and any test configuration you wrote. Install pytest and pytest-cov with `python -m pip install -r requirements-review.txt` from the repository root first.

Treat `exercises/` as shared reference material and keep your pull request scoped to your submission folder.

Mentors can use the [review guide](REVIEW.md) to check a specific submission commit.
