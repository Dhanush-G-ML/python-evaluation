# Topic 15: Pytest basics: exercises

In these exercises you do not write the program: you WRITE THE TESTS for a small program that is given to you (the code under test). Each exercise has its own folder in `starter/`, for example `starter/T15_E01/`. It holds the code under test (never change it) and, where useful, a test file that is empty or only partly filled in. Copy the folder to your submission's topic folder and write your tests in the copy.

Run the tests from inside the exercise folder:

- Windows (PowerShell or the VS Code terminal): `py -m pytest`
- Ubuntu: `python3 -m pytest`

Both forms put the current folder on the import path, so `import calculator` works. Every command in this document is written in the Windows form (`py -m pytest ...`); on Ubuntu write `python3 -m pytest ...` instead. Install once with `py -m pip install pytest pytest-cov` (Ubuntu: `python3 -m pip install pytest pytest-cov`, inside a virtual environment).

Use only the standard library plus `pytest` and `pytest-cov`. Test files are named `test_<something>.py`, test functions `test_<something>`.

How the expected output was made: every output block below was captured by running the real command on the trainer solutions with Python 3.12 on Ubuntu. The first line of each block (starting with `>`) is the command. The header lines pytest normally prints (platform, rootdir, plugins) are left out with `--no-header`, and the times (`in 0.02s`) will differ on your machine. Your own tests will have different names and may be more or fewer than the reference solution, so compare the idea (all green, or the failures described) and not every character. Where an exercise says "at least N tests", N is the minimum.

---

## T15-E01 - First test, assert and discovery rules

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** test functions, plain `assert`, `pytest.approx`, grouping tests in a class, file/function/class naming rules

**Code under test:** `starter/T15_E01/calculator.py` (functions `add`, `subtract`, `multiply`, `divide`)

**Starter test files:** `starter/T15_E01/test_calculator.py` and `starter/T15_E01/extra_tests.py` (both partly done, and both have a naming problem)

### Problem

Part A - discovery. Open `test_calculator.py` and `extra_tests.py`. Run `py -m pytest -v` in the folder and look at what pytest found. Then find out why the other tests were ignored, using these default rules:

- files are collected when the name matches `test_*.py` or `*_test.py`;
- inside them, functions that start with `test` are collected;
- classes are collected when the name starts with `Test` and has no `__init__`; methods inside must start with `test`.

Fix the names so that every test in the two files is collected, and move the tests from `extra_tests.py` into `test_calculator.py` (give the file a correct name or merge it).

Part B - write the tests. In `test_calculator.py` write plain tests with `assert` for:

- `add`: two positive numbers, two negative numbers, and `add(0.1, 0.2)` compared with `pytest.approx(0.3)` (floating point numbers are not exact);
- `subtract`: a normal case and a case with a negative result;
- `multiply`: a normal case and multiplying by zero (put the multiply tests in a class named `TestMultiply`);
- `divide`: `divide(10, 4)` is `2.5`, and the result is always a `float` (use `isinstance`).

Dividing by zero raises an exception; you will test that in T15-E02.

### Behaviours to test

| Function | Behaviour |
|----------|-----------|
| `add` | `add(2, 3) == 5`, `add(-2, -3) == -5`, `add(0.1, 0.2)` is about 0.3 |
| `subtract` | `subtract(5, 3) == 2`, `subtract(3, 5) == -2` |
| `multiply` | `multiply(4, 3) == 12`, `multiply(7, 0) == 0` |
| `divide` | `divide(10, 4) == 2.5`, `divide(10, 5)` is a float |

### Expected output

The starter folder as it is handed out. Only one test is collected, because `check_subtract` does not start with `test`, the class `CalculatorTests` does not start with `Test`, and `extra_tests.py` is not named like a test file:

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 1 item

test_calculator.py::test_add PASSED                                      [100%]

============================== 1 passed in 0.00s ===============================
```

When your tests are finished (the reference solution has 9 tests; write at least 8):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 9 items

test_calculator.py::test_add PASSED                                      [ 11%]
test_calculator.py::test_add_negative_numbers PASSED                     [ 22%]
test_calculator.py::test_add_floats_uses_approx PASSED                   [ 33%]
test_calculator.py::test_subtract PASSED                                 [ 44%]
test_calculator.py::test_subtract_gives_negative_result PASSED           [ 55%]
test_calculator.py::TestMultiply::test_multiply PASSED                   [ 66%]
test_calculator.py::TestMultiply::test_multiply_by_zero PASSED           [ 77%]
test_calculator.py::test_divide PASSED                                   [ 88%]
test_calculator.py::test_divide_always_returns_a_float PASSED            [100%]

============================== 9 passed in 0.01s ===============================
```

### Hints

- A test is just a function with an `assert`. If the assert is true the test passes; if it is false (or any exception is raised) the test fails.
- `from calculator import add` works because pytest puts the folder of the test file on the import path.
- `0.1 + 0.2 == 0.3` is `False` in Python. `pytest.approx(0.3)` compares with a small tolerance.
- `py -m pytest -v` prints one line per test. `py -m pytest -k multiply` runs only tests whose name contains "multiply".
- `py -m pytest --collect-only -q` lists what would run without running it.

### Acceptance checklist

- [ ] `py -m pytest -v` collects every test in the folder, and none are ignored because of their name.
- [ ] There are at least 8 tests and all pass.
- [ ] At least one test uses `pytest.approx` and at least one class `TestMultiply` is used.
- [ ] `calculator.py` was not changed.
- [ ] Each test checks one idea and has a name that says which.

---

## T15-E02 - Several inputs and pytest.raises

**Level:** Easy  |  **Estimated time:** 20 minutes  |  **Practises:** several asserts per test, boundary values, `pytest.raises`, `match=`, `excinfo`

**Code under test:** `starter/T15_E02/grade_calculator.py` (functions `percent_to_grade`, `average`, `has_passed`)

**Starter test file:** `starter/T15_E02/test_grade_calculator.py` (one test written, three TODOs)

### Problem

`percent_to_grade(score)` returns `A` for 90 and above, `B` for 80 and above, `C` for 70 and above, `D` for 60 and above and `F` otherwise. Scores outside 0 to 100 raise `ValueError`; a score that is not a number raises `TypeError`. `average(scores)` returns the mean of a list and raises `ValueError` for an empty list. `has_passed(score, pass_mark=50)` is true at or above the pass mark.

Write tests that check each function with several inputs, especially the boundary values (the number just at, and just below, each limit). Then test the errors with `pytest.raises`:

1. `percent_to_grade(101)` raises `ValueError`.
2. `percent_to_grade(-1)` raises `ValueError` and the message contains `between 0 and 100` (use `match=`).
3. `percent_to_grade("eighty")` raises `TypeError`; capture the exception with `as excinfo` and assert that `str(excinfo.value)` is `score must be a number`.
4. `average([])` raises `ValueError` mentioning `no scores`.
5. `average([80, 120])` raises `ValueError` (a bad score inside the list).
6. A valid call such as `percent_to_grade(50)` does not raise (a test with no `assert` that simply must not crash).

### Behaviours to test

| Input | Expected |
|-------|----------|
| 95, 85, 75, 65, 30 | A, B, C, D, F |
| 90, 80, 70, 60 | A, B, C, D (lower boundaries) |
| 89.99, 79, 69, 59 | B, C, D, F (just below) |
| 0 and 100 | F and A |
| `average([80, 90, 100])`, `average([50])`, `average([1, 2])` | 90, 50, 1.5 |
| `has_passed(50)`, `has_passed(49)`, `has_passed(70, pass_mark=75)` | True, False, False |
| 101, -1, "eighty", `[]`, `[80, 120]` | the errors listed above |

### Expected output

The reference solution (12 tests; write at least 10):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 12 items

test_grade_calculator.py::test_percent_to_grade_normal_scores PASSED     [  8%]
test_grade_calculator.py::test_percent_to_grade_lower_boundaries PASSED  [ 16%]
test_grade_calculator.py::test_percent_to_grade_just_below_boundaries PASSED [ 25%]
test_grade_calculator.py::test_percent_to_grade_extremes PASSED          [ 33%]
test_grade_calculator.py::test_average PASSED                            [ 41%]
test_grade_calculator.py::test_has_passed_default_and_custom_pass_mark PASSED [ 50%]
test_grade_calculator.py::test_score_above_100_raises_value_error PASSED [ 58%]
test_grade_calculator.py::test_negative_score_raises_value_error_with_message PASSED [ 66%]
test_grade_calculator.py::test_text_score_raises_type_error PASSED       [ 75%]
test_grade_calculator.py::test_average_of_empty_list_raises PASSED       [ 83%]
test_grade_calculator.py::test_average_rejects_a_bad_score_in_the_list PASSED [ 91%]
test_grade_calculator.py::test_valid_score_does_not_raise PASSED         [100%]

============================== 12 passed in 0.01s ==============================
```

If someone removes the range check from the code, the `raises` tests notice it. This is what a failing `pytest.raises` looks like (a deliberately broken copy of `grade_calculator.py`):

```text
> py -m pytest -q --tb=short
......FF..F.                                                             [100%]
=================================== FAILURES ===================================
___________________ test_score_above_100_raises_value_error ____________________
test_grade_calculator.py:46: in test_score_above_100_raises_value_error
    with pytest.raises(ValueError):
E   Failed: DID NOT RAISE ValueError
_____________ test_negative_score_raises_value_error_with_message ______________
test_grade_calculator.py:51: in test_negative_score_raises_value_error_with_message
    with pytest.raises(ValueError, match="between 0 and 100"):
E   Failed: DID NOT RAISE ValueError
_________________ test_average_rejects_a_bad_score_in_the_list _________________
test_grade_calculator.py:67: in test_average_rejects_a_bad_score_in_the_list
    with pytest.raises(ValueError):
E   Failed: DID NOT RAISE ValueError
=========================== short test summary info ============================
FAILED test_grade_calculator.py::test_score_above_100_raises_value_error - Fa...
FAILED test_grade_calculator.py::test_negative_score_raises_value_error_with_message
FAILED test_grade_calculator.py::test_average_rejects_a_bad_score_in_the_list
3 failed, 9 passed in 0.02s
```

### Hints

- Several `assert` lines in one test are fine for closely related inputs. The first failing assert stops that test, so separate tests give a clearer picture; the next exercises show a tidier way (`parametrize`).
- `with pytest.raises(ValueError):` passes only if the code inside the block raises that exception (or a subclass of it).
- `match="between 0 and 100"` is a regular expression searched in `str(exception)`. Escape special characters such as `.` or `(` with a backslash.
- `excinfo.value` is the exception object, `excinfo.type` its class.
- If no exception is raised, pytest fails the test with `DID NOT RAISE`.

### Acceptance checklist

- [ ] All boundary values (90, 89, 80, 79, 70, 69, 60, 59, 0 and 100) are tested.
- [ ] Each of the six error cases above is tested with `pytest.raises` (the message cases use `match=` or `excinfo`).
- [ ] At least 10 tests, all pass.
- [ ] A broken copy of the code (for example change `>= 90` to `> 90`) makes at least one of your tests fail.
- [ ] `grade_calculator.py` was not changed.

---

## T15-E03 - Testing a class and its state

**Level:** Easy  |  **Estimated time:** 20 minutes  |  **Practises:** creating objects in tests, testing state changes, tests that do not depend on each other, exceptions on a method, grouping tests in classes

**Code under test:** `starter/T15_E03/bank_account.py` (classes `BankAccount` and `InsufficientFundsError`)

**Starter test file:** `starter/T15_E03/test_bank_account.py` (one test written, a list of TODOs)

### Problem

A `BankAccount(owner, balance=0)` has a `balance` and a `history` (a list of `("deposit", amount)` and `("withdraw", amount)` entries). `deposit` and `withdraw` return the new balance and raise `ValueError` for amounts of zero or less. `withdraw` raises `InsufficientFundsError` when the amount is more than the balance. `transfer(other, amount)` moves money to another account. A failed operation must change nothing.

Write the tests. Every test creates its own account(s) inside the test, so no test depends on another. Group them in classes whose names start with `Test` (for example `TestOpening`, `TestDepositAndWithdraw`, `TestFailedOperationsChangeNothing`, `TestTransfer`). Test:

1. A new account keeps the owner and the opening balance; without a balance it starts at 0 with an empty history; a negative opening balance raises `ValueError`.
2. `deposit(50)` on a balance of 100 returns and shows 150; `withdraw(30)` returns and shows 70; withdrawing the whole balance is allowed.
3. The history lists every successful operation, oldest first.
4. Amounts of 0 and -10 raise `ValueError` for both deposit and withdraw, and the balance is unchanged.
5. An overdraft raises `InsufficientFundsError` (check the message with `match="balance is 100"`), and neither balance nor history changed.
6. The `history` you get back is a copy: appending to it does not change the account.
7. A transfer changes both balances; a failed transfer changes neither account; two accounts never share state.

### Behaviours to test

| Area | Behaviour |
|------|-----------|
| Opening | owner, balance, defaults, negative balance rejected |
| Deposit / withdraw | new balance returned and stored, whole balance can be withdrawn |
| History | successful operations recorded in order, copy returned |
| Errors | bad amounts, overdraft: exception raised, state unchanged |
| Transfer | both balances change, failed transfer changes nothing |
| Independence | separate accounts do not share state |

### Expected output

The reference solution (14 tests; write at least 12):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 14 items

test_bank_account.py::TestOpening::test_new_account_has_opening_balance PASSED [  7%]
test_bank_account.py::TestOpening::test_balance_defaults_to_zero_and_history_is_empty PASSED [ 14%]
test_bank_account.py::TestOpening::test_negative_opening_balance_is_rejected PASSED [ 21%]
test_bank_account.py::TestDepositAndWithdraw::test_deposit_increases_balance_and_returns_it PASSED [ 28%]
test_bank_account.py::TestDepositAndWithdraw::test_withdraw_decreases_balance_and_returns_it PASSED [ 35%]
test_bank_account.py::TestDepositAndWithdraw::test_withdraw_the_whole_balance_is_allowed PASSED [ 42%]
test_bank_account.py::TestDepositAndWithdraw::test_history_records_every_successful_operation PASSED [ 50%]
test_bank_account.py::TestDepositAndWithdraw::test_bad_amounts_raise_value_error[0] PASSED [ 57%]
test_bank_account.py::TestDepositAndWithdraw::test_bad_amounts_raise_value_error[-10] PASSED [ 64%]
test_bank_account.py::TestFailedOperationsChangeNothing::test_overdraft_raises_and_keeps_balance_and_history PASSED [ 71%]
test_bank_account.py::TestFailedOperationsChangeNothing::test_history_returned_is_a_copy PASSED [ 78%]
test_bank_account.py::TestTransfer::test_transfer_moves_money_between_accounts PASSED [ 85%]
test_bank_account.py::TestTransfer::test_failed_transfer_changes_neither_account PASSED [ 92%]
test_bank_account.py::TestTransfer::test_two_accounts_do_not_share_state PASSED [100%]

============================== 14 passed in 0.01s ==============================
```

### Hints

- Write each test in three steps: arrange (create the account), act (call the method), assert (check balance and history).
- To test that something did NOT change, check the value after the failing call, outside the `with pytest.raises(...)` block (code after the exception inside the block never runs).
- Check the state, not only the return value: `account.balance` and `account.history`.
- `@pytest.mark.parametrize` can repeat a test with several amounts. You may use it already, the next exercise explains it.

### Acceptance checklist

- [ ] At least 12 tests, in at least three classes named `Test...`, and all pass.
- [ ] Every test builds its own accounts; the tests pass in any order (try `py -m pytest -k "transfer"` alone).
- [ ] Failed operations are checked for unchanged balance and history.
- [ ] A broken copy (for example `if amount > self._balance` replaced with `if False`) makes at least one of your tests fail.
- [ ] `bank_account.py` was not changed.

---

## T15-E04 - Parametrize and reading failure output

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** `@pytest.mark.parametrize`, `ids=`, `pytest.param`, reading a failure report, deciding whether the test or the code is wrong

**Code under test:** `starter/T15_E04/temperature.py` (functions `c_to_f`, `f_to_c`, `c_to_k`, `describe`)

**Starter test file:** `starter/T15_E04/test_temperature.py` (five tests, four of them fail on purpose)

### Problem

Part A - read the failures. Run `py -m pytest` in the folder. Four tests fail. For each one, read the failure report from the bottom: the `E` lines say what was compared, the line with `>` marks the failing statement, and the last line names the exception. Decide for each failure whether the TEST or the CODE is wrong. The code in `temperature.py` is correct, as its docstrings say; fix the tests:

- `test_boiling_point_in_fahrenheit` has a wrong expected value;
- `test_body_temperature_in_celsius` compares floating point numbers with `==` (use `pytest.approx`);
- `test_fifteen_degrees_is_cold` disagrees with the docstring of `describe` (look at the boundary);
- `test_below_absolute_zero` does not expect the exception that is documented.

Part B - parametrize. Add parametrized tests (one test function each, many rows of data):

1. `c_to_f` for `(0, 32)`, `(100, 212)`, `(-40, -40)`, `(37, 98.6)`, `(-273.15, -459.67)`, compared with `pytest.approx`.
2. `f_to_c` for `(32, 0)`, `(212, 100)`, `(-40, -40)`, `(98.6, 37)` with readable ids: `ids=["freezing", "boiling", "equal-point", "body"]`.
3. `describe` for the boundaries `-10, 0, 0.1, 14.9, 15, 24.9, 25, 40` with the expected words.
4. `c_to_k` raises `ValueError` for `-273.16` and `-500` (parametrize `celsius`, use `pytest.raises` inside).
5. One test that `c_to_k(-273.15)` is accepted and gives about 0.

### Behaviours to test

| Function | Behaviour |
|----------|-----------|
| `c_to_f` | the five pairs above |
| `f_to_c` | the four pairs above |
| `describe` | `<= 0` freezing, below 15 cold, below 25 mild, otherwise hot |
| `c_to_k` | below -273.15 raises `ValueError`; -273.15 itself is allowed |

### Expected output

The starter file as handed out (read this report carefully; the 4 failures have different causes):

```text
> py -m pytest -q --tb=short
.FFFF                                                                    [100%]
=================================== FAILURES ===================================
_______________________ test_boiling_point_in_fahrenheit _______________________
test_temperature.py:11: in test_boiling_point_in_fahrenheit
    assert c_to_f(100) == 112
E   assert 212.0 == 112
E    +  where 212.0 = c_to_f(100)
_______________________ test_body_temperature_in_celsius _______________________
test_temperature.py:15: in test_body_temperature_in_celsius
    assert f_to_c(100) == 37.78
E   assert 37.77777777777778 == 37.78
E    +  where 37.77777777777778 = f_to_c(100)
_________________________ test_fifteen_degrees_is_cold _________________________
test_temperature.py:19: in test_fifteen_degrees_is_cold
    assert describe(15) == "cold"
E   AssertionError: assert 'mild' == 'cold'
E
E     - cold
E     + mild
___________________________ test_below_absolute_zero ___________________________
test_temperature.py:23: in test_below_absolute_zero
    assert c_to_k(-300) == 0
           ^^^^^^^^^^^^
temperature.py:17: in c_to_k
    raise ValueError("temperature is below absolute zero")
E   ValueError: temperature is below absolute zero
=========================== short test summary info ============================
FAILED test_temperature.py::test_boiling_point_in_fahrenheit - assert 212.0 =...
FAILED test_temperature.py::test_body_temperature_in_celsius - assert 37.7777...
FAILED test_temperature.py::test_fifteen_degrees_is_cold - AssertionError: as...
FAILED test_temperature.py::test_below_absolute_zero - ValueError: temperatur...
4 failed, 1 passed in 0.01s
```

The reference solution after the fix and the parametrized tests (25 tests; write at least 20):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 25 items

test_temperature.py::test_freezing_point_in_fahrenheit PASSED            [  4%]
test_temperature.py::test_boiling_point_in_fahrenheit PASSED             [  8%]
test_temperature.py::test_body_temperature_in_celsius PASSED             [ 12%]
test_temperature.py::test_fifteen_degrees_is_mild PASSED                 [ 16%]
test_temperature.py::test_below_absolute_zero_raises PASSED              [ 20%]
test_temperature.py::test_c_to_f[0-32] PASSED                            [ 24%]
test_temperature.py::test_c_to_f[100-212] PASSED                         [ 28%]
test_temperature.py::test_c_to_f[-40--40] PASSED                         [ 32%]
test_temperature.py::test_c_to_f[37-98.6] PASSED                         [ 36%]
test_temperature.py::test_c_to_f[-273.15--459.67] PASSED                 [ 40%]
test_temperature.py::test_f_to_c[freezing] PASSED                        [ 44%]
test_temperature.py::test_f_to_c[boiling] PASSED                         [ 48%]
test_temperature.py::test_f_to_c[equal-point] PASSED                     [ 52%]
test_temperature.py::test_f_to_c[body] PASSED                            [ 56%]
test_temperature.py::test_describe_boundaries[-10-freezing] PASSED       [ 60%]
test_temperature.py::test_describe_boundaries[0-freezing] PASSED         [ 64%]
test_temperature.py::test_describe_boundaries[0.1-cold] PASSED           [ 68%]
test_temperature.py::test_describe_boundaries[14.9-cold] PASSED          [ 72%]
test_temperature.py::test_describe_boundaries[15-mild] PASSED            [ 76%]
test_temperature.py::test_describe_boundaries[24.9-mild] PASSED          [ 80%]
test_temperature.py::test_describe_boundaries[25-hot] PASSED             [ 84%]
test_temperature.py::test_describe_boundaries[40-hot] PASSED             [ 88%]
test_temperature.py::test_c_to_k_rejects_impossible_temperatures[-273.16] PASSED [ 92%]
test_temperature.py::test_c_to_k_rejects_impossible_temperatures[-500] PASSED [ 96%]
test_temperature.py::test_c_to_k_accepts_absolute_zero PASSED            [100%]

============================== 25 passed in 0.02s ==============================
```

A parametrized failure names the failing row. This is a deliberately broken copy of `describe` (`celsius <= 15` instead of `celsius < 15`):

```text
> py -m pytest -q --tb=short
...F..............F......                                                [100%]
=================================== FAILURES ===================================
_________________________ test_fifteen_degrees_is_mild _________________________
test_temperature.py:19: in test_fifteen_degrees_is_mild
    assert describe(15) == "mild"
E   AssertionError: assert 'cold' == 'mild'
E
E     - mild
E     + cold
______________________ test_describe_boundaries[15-mild] _______________________
test_temperature.py:69: in test_describe_boundaries
    assert describe(celsius) == expected
E   AssertionError: assert 'cold' == 'mild'
E
E     - mild
E     + cold
=========================== short test summary info ============================
FAILED test_temperature.py::test_fifteen_degrees_is_mild - AssertionError: as...
FAILED test_temperature.py::test_describe_boundaries[15-mild] - AssertionErro...
2 failed, 23 passed in 0.02s
```

### Hints

- `@pytest.mark.parametrize("a, b", [(1, 2), (3, 4)])` runs the test once for each tuple. The names in the string must match the function parameters.
- In the report, `test_c_to_f[100-212]` is the test name followed by the values (or your own `ids`) in square brackets. Use `py -m pytest -k "boiling"` to run one row.
- When a failure is unclear, run only that test with `py -m pytest -k name --tb=long`.
- `pytest.approx(37.78, abs=0.01)` accepts values within 0.01 of 37.78. Plain `pytest.approx(x)` has a relative tolerance of one in a million.
- When the test and the code disagree, decide from the specification (the docstring), not from which is easier to change.

### Acceptance checklist

- [ ] The four starter failures are fixed by changing the tests, and the explanation of each cause is written as a comment or short note.
- [ ] At least four parametrized tests, one of them with your own `ids`.
- [ ] Every temperature boundary of `describe` is covered.
- [ ] At least 20 tests, all pass.
- [ ] `temperature.py` was not changed.

---

## T15-E05 - Fixtures: setup, yield teardown and scope

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** `@pytest.fixture`, fixtures that use other fixtures, `yield` and teardown, `autouse`, fixture scope, `--setup-show`

**Code under test:** `starter/T15_E05/bank.py` (class `Bank`)

**Starter test file:** `starter/T15_E05/test_bank.py` (one test written, four TODOs)

### Problem

A `Bank` opens accounts (`open_account(owner, deposit=0)` returns 1, 2, 3, ...), keeps balances (`balance`, `deposit`, `account_count`, `total_deposits`) and can be closed (`close()`). Every `Bank` registers itself in the class list `Bank.open_banks` and removes itself when it is closed, so a test that forgets to close its bank leaves it in that list.

Build these fixtures in `test_bank.py` and use them:

1. `bank`: creates `Bank("Test Bank")`, hands it to the test with `yield`, and closes it afterwards (the code after `yield` is the teardown and runs even when the test fails). Rewrite the first test to use it.
2. `bank_with_two_accounts`: uses the `bank` fixture, opens an account for Asha with 100 and one for Ravi with 50, and returns `(bank, first_number, second_number)`.
3. `no_open_banks_left`: a module-scoped, autouse fixture that does nothing before the tests and, after the last test of the file, asserts that `Bank.open_banks == []`. It is a leak check for your other fixtures.
4. `shared_bank`: a module-scoped fixture (one `Bank("Shared Bank")` for all tests of the file, closed at the end).

Write the tests:

- a new bank has no accounts; account numbers start at 1 and go up; a negative opening deposit raises `ValueError`;
- `deposit` changes one balance and not the other; `total_deposits` adds all accounts (use `bank_with_two_accounts`);
- a closed bank raises `RuntimeError` (message contains `closed`) when you open an account;
- scope demonstration: one test that opens an account in `shared_bank` and asserts the count is 1, and a second test (defined after it) that asserts the count is still 1, because with module scope both tests received the same bank.

Then run the tests with `--setup-show` and read when each fixture is set up and torn down.

### Behaviours to test

| Fixture or area | What to check |
|-----------------|---------------|
| `bank` (function scope) | each test gets a fresh, empty bank; it is closed afterwards |
| `bank_with_two_accounts` | numbers 1 and 2, balances 100 and 50, total 150 |
| `no_open_banks_left` | after the module, no bank is left open |
| `shared_bank` (module scope) | the second test sees the account the first test opened |
| `Bank` | closed bank rejects `open_account`, negative deposit rejected |

### Expected output

The reference solution (9 tests; write at least 8):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 9 items

test_bank.py::test_new_bank_has_no_accounts PASSED                       [ 11%]
test_bank.py::test_open_account_numbers_start_at_one PASSED              [ 22%]
test_bank.py::test_negative_opening_deposit_is_rejected PASSED           [ 33%]
test_bank.py::test_deposit_changes_one_balance PASSED                    [ 44%]
test_bank.py::test_total_deposits_adds_all_accounts PASSED               [ 55%]
test_bank.py::test_closed_bank_rejects_new_accounts PASSED               [ 66%]
test_bank.py::test_function_scope_gives_each_test_a_fresh_bank PASSED    [ 77%]
test_bank.py::test_module_scope_first_test_fills_the_shared_bank PASSED  [ 88%]
test_bank.py::test_module_scope_second_test_sees_the_same_bank PASSED    [100%]

============================== 9 passed in 0.01s ===============================
```

Setup and teardown for one test. Fixture names are prefixed with the scope letter: `F` function, `M` module. Fixtures that need other fixtures are set up after them and torn down before them:

```text
> py -m pytest -v --setup-show -k test_deposit_changes_one_balance
============================= test session starts ==============================
collecting ... collected 9 items / 8 deselected / 1 selected

test_bank.py::test_deposit_changes_one_balance
    SETUP    M no_open_banks_left
        SETUP    F bank
        SETUP    F bank_with_two_accounts (fixtures used: bank)
        test_bank.py::test_deposit_changes_one_balance (fixtures used: bank, bank_with_two_accounts, no_open_banks_left) PASSED
        TEARDOWN F bank_with_two_accounts
        TEARDOWN F bank
    TEARDOWN M no_open_banks_left

======================= 1 passed, 8 deselected in 0.01s ========================
```

The module-scoped fixture is set up once and torn down at the end of the module, after the last test that uses it:

```text
> py -m pytest -v --setup-show -k module_scope
============================= test session starts ==============================
collecting ... collected 9 items / 7 deselected / 2 selected

test_bank.py::test_module_scope_first_test_fills_the_shared_bank
    SETUP    M no_open_banks_left
    SETUP    M shared_bank
        test_bank.py::test_module_scope_first_test_fills_the_shared_bank (fixtures used: no_open_banks_left, shared_bank) PASSED
test_bank.py::test_module_scope_second_test_sees_the_same_bank
        test_bank.py::test_module_scope_second_test_sees_the_same_bank (fixtures used: no_open_banks_left, shared_bank) PASSED
    TEARDOWN M shared_bank
    TEARDOWN M no_open_banks_left

======================= 2 passed, 7 deselected in 0.01s ========================
```

If `Bank.close()` forgets to unregister the bank (a deliberately broken copy), the leak check reports an ERROR in the teardown of the last test, even though every test itself passed:

```text
> py -m pytest -q --tb=short
.........E                                                               [100%]
==================================== ERRORS ====================================
____ ERROR at teardown of test_module_scope_second_test_sees_the_same_bank _____
test_bank.py:10: in no_open_banks_left
    assert left_open == [], "a test left a bank open"
E   AssertionError: a test left a bank open
E   assert ['Test Bank',...st Bank', ...] == []
E
E     Left contains 8 more items, first extra item: 'Test Bank'
E     Use -v to get more diff
=========================== short test summary info ============================
ERROR test_bank.py::test_module_scope_second_test_sees_the_same_bank - Assert...
9 passed, 1 error in 0.02s
```

### Hints

- A fixture is a function with `@pytest.fixture`. A test asks for it by writing its name as a parameter. pytest runs the fixture first and passes the returned value.
- Code before `yield` is setup, code after it is teardown. The teardown runs after the test even if the test failed.
- Default scope is `function` (a new value for every test). `scope="module"` creates it once per test file, `scope="session"` once per run.
- `autouse=True` applies the fixture to every test in its scope without naming it.
- Tests that share a module-scoped object depend on each other and on order. That is acceptable for expensive resources that tests only read, but avoid sharing objects that tests change.
- `py -m pytest --setup-show` prints SETUP and TEARDOWN lines; `py -m pytest --fixtures` lists the fixtures pytest knows about.

### Acceptance checklist

- [ ] The `bank` fixture uses `yield` and closes the bank in the teardown.
- [ ] `bank_with_two_accounts` uses the `bank` fixture.
- [ ] The leak-check fixture is module scoped and autouse, and the whole file passes with it.
- [ ] You can explain from the `--setup-show` output why the two module-scope tests share one bank.
- [ ] A broken copy (for example make `close()` skip `Bank.open_banks.remove(self)`) produces an error or failure in your suite.
- [ ] `bank.py` was not changed.

---

## T15-E06 - Fixtures with params and conftest.py

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** `@pytest.fixture(params=...)`, `request.param`, `ids=`, `conftest.py`, sharing fixtures between test files

**Code under test:** `starter/T15_E06/string_helper.py` (functions `slugify`, `truncate`, `word_count`, `is_palindrome`)

**Starter test file:** `starter/T15_E06/test_slugify.py` (uses two fixtures that do not exist yet)

### Problem

Part A - the missing fixtures. Run `py -m pytest`: both tests in `test_slugify.py` show an error `fixture '...' not found`. Create `conftest.py` in the same folder. pytest reads it automatically and every test file in the folder can use its fixtures without importing them. Put these two fixtures in it:

1. `hello_variants`: a fixture with `params`, four spellings of the same title, with ids: `"Hello World"` (`plain`), `"  Hello   World  "` (`extra-spaces`), `"HELLO-world"` (`dash-and-caps`) and `"hello_world!"` (`underscore-and-bang`). It returns `request.param`. Every test that uses it runs four times.
2. `sentence`: a plain fixture returning `"Pytest makes testing pleasant, even for beginners"`.

Part B - tests in two files. In `test_slugify.py` test that `slugify(hello_variants)` is `hello-world` for every variant, that the slug of `sentence` has no spaces and equals `pytest-makes-testing-pleasant-even-for-beginners`, and that the slug of `""` is `""`.

Create a second file `test_text_stats.py` that uses the SAME `sentence` fixture from `conftest.py` and tests:

- `word_count(sentence) == 7`;
- a fixture `max_length` defined inside this file with `params=[5, 10, 20]` and ids `len5`, `len10`, `len20`; a test that `len(truncate(sentence, max_length)) <= max_length` (three runs);
- `truncate(sentence, 10) == "Pytest ..."`, short text stays unchanged, text of exactly the limit is not shortened, and a limit shorter than the suffix raises `ValueError`;
- `is_palindrome` is true for `"A man, a plan, a canal: Panama"` and false for `"pytest"`.

### Behaviours to test

| Function | Behaviour |
|----------|-----------|
| `slugify` | lowercase, runs of other characters become one `-`, no dash at either end |
| `truncate` | at most `length` characters; ends with `...` when shortened; short text unchanged; length below the suffix raises |
| `word_count` | counts words split on whitespace |
| `is_palindrome` | ignores case, spaces and punctuation |

### Expected output

The starter folder before you create `conftest.py`:

```text
> py -m pytest -q --tb=short
EE                                                                       [100%]
==================================== ERRORS ====================================
________ ERROR at setup of test_every_hello_variant_gives_the_same_slug ________
file ./test_slugify.py, line 4
  def test_every_hello_variant_gives_the_same_slug(hello_variants):
E       fixture 'hello_variants' not found
>       available fixtures: capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, cov, doctest_namespace, monkeypatch, no_cover, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, subtests, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

./test_slugify.py:4
__________________ ERROR at setup of test_slug_has_no_spaces ___________________
file ./test_slugify.py, line 8
  def test_slug_has_no_spaces(sentence):
E       fixture 'sentence' not found
>       available fixtures: capfd, capfdbinary, caplog, capsys, capsysbinary, capteesys, cov, doctest_namespace, monkeypatch, no_cover, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, subtests, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

./test_slugify.py:8
=========================== short test summary info ============================
ERROR test_slugify.py::test_every_hello_variant_gives_the_same_slug
ERROR test_slugify.py::test_slug_has_no_spaces
2 errors in 0.00s
```

The reference solution (17 tests: the four `hello_variants` runs and the three `max_length` runs are separate tests; write at least 14):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 17 items

test_slugify.py::test_every_hello_variant_gives_the_same_slug[plain] PASSED [  5%]
test_slugify.py::test_every_hello_variant_gives_the_same_slug[extra-spaces] PASSED [ 11%]
test_slugify.py::test_every_hello_variant_gives_the_same_slug[dash-and-caps] PASSED [ 17%]
test_slugify.py::test_every_hello_variant_gives_the_same_slug[underscore-and-bang] PASSED [ 23%]
test_slugify.py::test_slug_has_no_spaces PASSED                          [ 29%]
test_slugify.py::test_slug_is_lowercase_and_dash_separated PASSED        [ 35%]
test_slugify.py::test_empty_text_gives_empty_slug PASSED                 [ 41%]
test_text_stats.py::test_word_count_of_the_shared_sentence PASSED        [ 47%]
test_text_stats.py::test_truncate_never_exceeds_the_limit[len5] PASSED   [ 52%]
test_text_stats.py::test_truncate_never_exceeds_the_limit[len10] PASSED  [ 58%]
test_text_stats.py::test_truncate_never_exceeds_the_limit[len20] PASSED  [ 64%]
test_text_stats.py::test_truncate_adds_the_suffix_when_shortening PASSED [ 70%]
test_text_stats.py::test_truncate_leaves_short_text_alone PASSED         [ 76%]
test_text_stats.py::test_truncate_exact_length_is_not_shortened PASSED   [ 82%]
test_text_stats.py::test_truncate_rejects_a_limit_shorter_than_the_suffix PASSED [ 88%]
test_text_stats.py::test_palindrome_ignores_case_and_punctuation PASSED  [ 94%]
test_text_stats.py::test_non_palindrome PASSED                           [100%]

============================== 17 passed in 0.01s ==============================
```

If `slugify` forgets to remove leading and trailing dashes (a deliberately broken copy), only the variants that have such characters fail, and the ids tell you which:

```text
> py -m pytest -q --tb=line
.F.F.............                                                        [100%]
=================================== FAILURES ===================================
E   AssertionError: assert '-hello-world-' == 'hello-world'

      - hello-world
      + -hello-world-
      ? +           +
./test_slugify.py:5: AssertionError: assert '-hello-world-' == 'hello-world'
E   AssertionError: assert 'hello-world-' == 'hello-world'

      - hello-world
      + hello-world-
      ?            +
./test_slugify.py:5: AssertionError: assert 'hello-world-' == 'hello-world'
=========================== short test summary info ============================
FAILED test_slugify.py::test_every_hello_variant_gives_the_same_slug[extra-spaces]
FAILED test_slugify.py::test_every_hello_variant_gives_the_same_slug[underscore-and-bang]
2 failed, 15 passed in 0.01s
```

### Hints

- For a fixture with `params`, pytest runs every test that uses the fixture once per parameter. The fixture function receives the current value as `request.param`.
- `ids=[...]` must have one name per parameter. Without it pytest invents names like `hello_variants0`.
- A fixture in `conftest.py` is visible to all test files in that folder and below. A fixture defined in a test file is visible only in that file. If both exist with the same name, the closer one wins.
- Never `import` from `conftest.py` in a test file; just use the fixture name as a parameter.
- `py -m pytest --fixtures` shows where each fixture is defined.

### Acceptance checklist

- [ ] `conftest.py` exists and holds `hello_variants` (with `params` and `ids`) and `sentence`.
- [ ] `test_slugify.py` and `test_text_stats.py` both use the `sentence` fixture without importing it.
- [ ] A fixture with params is used by at least one test, and `-v` shows four separate runs of it.
- [ ] At least 14 tests, all pass.
- [ ] A broken copy of `slugify` (without `.strip("-")`) makes only the matching variants fail.
- [ ] `string_helper.py` was not changed.

---

## T15-E07 - Markers 1: skip, skipif and xfail

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** `@pytest.mark.skip`, `@pytest.mark.skipif`, `@pytest.mark.xfail` with `reason` and `strict`, reading `s`, `x`, `X` and the `-r` report

**Code under test:** `starter/T15_E07/price.py` (functions `apply_discount`, `format_price`, `to_cents`, `line_separator`)

**Starter test file:** `starter/T15_E07/test_price.py` (two tests written, imports ready)

### Problem

Built-in markers change what pytest does with a test without changing the test body. Add these tests to `test_price.py`:

1. `test_apply_discount` and `test_format_price` (given): `apply_discount(200, 25) == 150`, `format_price(5) == "5.00 USD"`.
2. `test_refund_is_calculated`: a test for a feature that does not exist yet. Mark it `@pytest.mark.skip(reason="refunds are not implemented yet")`. It is never run.
3. `test_line_separator_on_posix`: `line_separator() == "\n"`, with `@pytest.mark.skipif(sys.platform == "win32", reason="Linux and macOS line endings")`.
4. `test_line_separator_on_windows`: `line_separator() == "\r\n"`, with `@pytest.mark.skipif(sys.platform != "win32", reason="Windows line endings")`. On any machine exactly one of tests 3 and 4 runs and the other is skipped.
5. `test_copy_replace_exists`: asserts `hasattr(copy, "replace")` (a function added in Python 3.13) with `@pytest.mark.skipif(sys.version_info < (3, 13), reason="copy.replace needs Python 3.13")`. On Python 3.12 it is skipped.
6. `test_to_cents_of_19_99`: asserts `to_cents(19.99) == 1999`. The code has a documented bug (see the docstring at the top of `price.py`): it returns 1998. Mark the test `@pytest.mark.xfail(reason="known bug: to_cents truncates instead of rounding", strict=True)`. It is an expected failure.
7. `test_to_cents_of_a_whole_price`: asserts `to_cents(2.5) == 250` with `@pytest.mark.xfail(reason="not sure this one works, check later")` (not strict). This one passes, which pytest reports as "unexpectedly passed".

Run with `py -m pytest -v -rsxX`. The `-r` option adds a short summary: `s` skipped (with reason), `x` expected failures, `X` unexpected passes.

Part B - strict. Change the code temporarily: in `price.py` replace `int(price * 100)` with `round(price * 100)`, run again, and read what happens to test 6 (and to test 7). Change the code back afterwards.

### Behaviours to test

| Marker | Used for | Result symbol |
|--------|----------|---------------|
| `skip` | a test that must not run at all | `s` (SKIPPED) |
| `skipif(condition, reason=...)` | a test that only makes sense on some systems or versions | `s` when the condition is true, otherwise the normal `.` |
| `xfail(reason=...)` | a test for a known bug | `x` (XFAIL) while it still fails |
| `xfail` (not strict) that passes | | `X` (XPASS): reported but the run still succeeds |
| `xfail(strict=True)` that passes | | shown as FAILED with the text `[XPASS(strict)]`: the run fails, which tells you the bug is fixed and the marker must go |

### Expected output

The reference solution on Ubuntu with Python 3.12. The summary at the bottom lists the skipped tests with their reasons, the expected failure and the unexpected pass. On Windows the two line-separator tests swap places (the Windows test runs and the POSIX test is skipped), but the counts stay the same:

```text
> py -m pytest -v -rsxX
============================= test session starts ==============================
collecting ... collected 8 items

test_price.py::test_apply_discount PASSED                                [ 12%]
test_price.py::test_format_price PASSED                                  [ 25%]
test_price.py::test_refund_is_calculated SKIPPED (refunds are not im...) [ 37%]
test_price.py::test_line_separator_on_posix PASSED                       [ 50%]
test_price.py::test_line_separator_on_windows SKIPPED (Windows line ...) [ 62%]
test_price.py::test_copy_replace_exists SKIPPED (copy.replace needs ...) [ 75%]
test_price.py::test_to_cents_of_19_99 XFAIL (known bug: to_cents tru...) [ 87%]
test_price.py::test_to_cents_of_a_whole_price XPASS (not sure this o...) [100%]

=================================== XPASSES ====================================
=========================== short test summary info ============================
SKIPPED [1] test_price.py:17: refunds are not implemented yet
SKIPPED [1] test_price.py:27: Windows line endings
SKIPPED [1] test_price.py:32: copy.replace needs Python 3.13
XFAIL test_price.py::test_to_cents_of_19_99 - known bug: to_cents truncates instead of rounding
XPASS test_price.py::test_to_cents_of_a_whole_price - not sure this one works, check later
============== 3 passed, 3 skipped, 1 xfailed, 1 xpassed in 0.01s ==============
```

After the bug in `to_cents` is fixed (a copy of `price.py` with `round` instead of `int`), the strict marker turns the unexpected pass into a failure:

```text
> py -m pytest -v -rsxX --tb=short
============================= test session starts ==============================
collecting ... collected 8 items

test_price.py::test_apply_discount PASSED                                [ 12%]
test_price.py::test_format_price PASSED                                  [ 25%]
test_price.py::test_refund_is_calculated SKIPPED (refunds are not im...) [ 37%]
test_price.py::test_line_separator_on_posix PASSED                       [ 50%]
test_price.py::test_line_separator_on_windows SKIPPED (Windows line ...) [ 62%]
test_price.py::test_copy_replace_exists SKIPPED (copy.replace needs ...) [ 75%]
test_price.py::test_to_cents_of_19_99 FAILED                             [ 87%]
test_price.py::test_to_cents_of_a_whole_price XPASS (not sure this o...) [100%]

=================================== FAILURES ===================================
____________________________ test_to_cents_of_19_99 ____________________________
[XPASS(strict)] known bug: to_cents truncates instead of rounding
=================================== XPASSES ====================================
=========================== short test summary info ============================
SKIPPED [1] test_price.py:17: refunds are not implemented yet
SKIPPED [1] test_price.py:27: Windows line endings
SKIPPED [1] test_price.py:32: copy.replace needs Python 3.13
XPASS test_price.py::test_to_cents_of_a_whole_price - not sure this one works, check later
============== 1 failed, 3 passed, 3 skipped, 1 xpassed in 0.01s ===============
```

### Hints

- Symbols in the short progress output: `.` passed, `F` failed, `E` error, `s` skipped, `x` expected failure, `X` unexpected pass. In `-v` mode you see the words SKIPPED, XFAIL, XPASS.
- `skip` always skips. `skipif` takes a condition (a Python expression that is true or false) and a `reason=`; always give a reason, because it is shown in the report.
- `xfail` runs the test and records the failure as expected, so the suite stays green. It is for known bugs that are written down. Do not use it to hide tests you do not understand.
- `strict=True` makes an unexpected pass a failure. Use it for known bugs so that you notice the day the bug is fixed.
- You can also skip inside a test with `pytest.skip("reason")` and mark expected failures from a condition: `@pytest.mark.xfail(sys.platform == "win32", reason="...")`.

### Acceptance checklist

- [ ] The three kinds of skip are used (`skip`, `skipif` on the platform, `skipif` on the Python version), each with a `reason`.
- [ ] One `xfail` with `strict=True` and one without; both have a `reason`.
- [ ] `py -m pytest -v -rsxX` runs without failures, and you can name the test behind each `s`, `x` and `X` in the output.
- [ ] After the temporary code change, you can explain why the strict `xfail` test now fails. The code is changed back.
- [ ] `price.py` is unchanged at the end.

---

## T15-E08 - Markers 2: custom markers, pytest.ini and -m

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** custom markers (`smoke`, `slow`), registering markers in `pytest.ini`, `--strict-markers`, selecting with `-m`, marks on classes, marks inside `parametrize` with `pytest.param(..., marks=...)`

**Code under test:** `starter/T15_E08/shipping.py` (functions `shipping_cost`, `delivery_days`, `bulk_quote`; the last one is slow on purpose)

**Starter test file:** `starter/T15_E08/test_shipping.py` (three tests, already using `smoke` and `slow`)

### Problem

Part A - the warning. Run `py -m pytest -v` in the folder. The tests pass, but pytest warns that `smoke` and `slow` are unknown marks (`PytestUnknownMarkWarning`), because a typo in a marker name would silently select nothing. Then run `py -m pytest --strict-markers` and see that it becomes an error.

Part B - register the markers. Create `pytest.ini` in the folder:

```ini
[pytest]
markers =
    smoke: fast checks that must always pass
    slow: tests that take noticeably longer (deselect with -m "not slow")
addopts = --strict-markers
```

`addopts` adds `--strict-markers` to every run. Check with `py -m pytest --markers` that your two markers are listed with their descriptions, and run again: no warnings.

Part C - write the tests. In `test_shipping.py` have these tests (the three given ones can be reshaped):

1. `shipping_cost(2) == 5.99` and `shipping_cost(2, "express") == 10.99`, both marked `@pytest.mark.smoke`.
2. A class `TestFreeShipping` marked `@pytest.mark.smoke` (a mark on a class applies to every test inside): an order total of 50 ships free (`shipping_cost(2, order_total=50) == 0.0`), a total of 49.99 pays 5.99.
3. Unknown method (`"pigeon"`) raises `ValueError` matching `unknown shipping method`; weight 0 raises `ValueError` matching `weight`. No marks.
4. `bulk_quote` parametrized with `(10, 1, 40.41)`, `(1, 1, 4.04)` and `(100, 2, 539.1)` for `(parcels, weight, expected)`, the whole test marked `@pytest.mark.slow`.
5. `delivery_days` parametrized with `pytest.param(..., marks=...)` so that single rows carry their own marks:

| country | days | marks on the row |
|---------|------|------------------|
| IN | 3 | `pytest.mark.smoke` |
| US | 6 | `[pytest.mark.smoke, pytest.mark.slow]` |
| UK | 5 | none |
| NZ | 10 | none |
| FR | 4 | `pytest.mark.skip(reason="France rate not decided")` |
| DE | 5 | `pytest.mark.xfail(reason="DE is not in the table, so it takes 10 days")` |

Part D - select tests. Use `-m` with a marker expression and see how many tests are deselected. Expressions can combine marker names with `and`, `or`, `not` and brackets. `--collect-only -q` lists what a selection would run without running it.

### Behaviours to test

| Marker or mark | What it selects |
|----------------|-----------------|
| `-m smoke` | the shipping cost checks, the class `TestFreeShipping`, and the rows IN and US |
| `-m slow` | the three `bulk_quote` cases and the row US |
| `-m "not slow"` | everything except those four |
| `-m "smoke and not slow"` | smoke tests that are quick |
| `-m "smoke and slow"` | only the row US (it has both marks) |
| `-m "smoke or slow"` | anything with either mark |

### Expected output

Before `pytest.ini` exists (the starter folder as handed out):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 3 items

test_shipping.py::test_standard_shipping_cost PASSED                     [ 33%]
test_shipping.py::test_bulk_quote_for_ten_parcels PASSED                 [ 66%]
test_shipping.py::test_delivery_days_to_india PASSED                     [100%]

=============================== warnings summary ===============================
test_shipping.py:6
  ./test_shipping.py:6: PytestUnknownMarkWarning: Unknown pytest.mark.smoke - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.smoke

test_shipping.py:11
  ./test_shipping.py:11: PytestUnknownMarkWarning: Unknown pytest.mark.slow - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.slow

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
======================== 3 passed, 2 warnings in 0.21s =========================
```

The same folder with `--strict-markers`, which turns the unknown markers into an error:

```text
> py -m pytest --strict-markers
============================= test session starts ==============================
collected 0 items / 1 error

==================================== ERRORS ====================================
______________________ ERROR collecting test_shipping.py _______________________
'smoke' not found in `markers` configuration option
=========================== short test summary info ============================
ERROR test_shipping.py - Failed: 'smoke' not found in `markers` configuration...
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.05s ===============================
```

The registered markers (only the lines for `smoke` and `slow` are shown; `py -m pytest --markers` also lists the built-in markers):

```text
> py -m pytest --markers
@pytest.mark.smoke: fast checks that must always pass
@pytest.mark.slow: tests that take noticeably longer (deselect with -m "not slow")
```

The reference solution with all tests (15 tests; write at least 13). Note the `s` for France and `x` for Germany:

```text
> py -m pytest -v -rsx
============================= test session starts ==============================
collecting ... collected 15 items

test_shipping.py::test_standard_shipping_cost PASSED                     [  6%]
test_shipping.py::test_express_shipping_cost PASSED                      [ 13%]
test_shipping.py::TestFreeShipping::test_free_from_fifty PASSED          [ 20%]
test_shipping.py::TestFreeShipping::test_paid_below_fifty PASSED         [ 26%]
test_shipping.py::test_unknown_method_is_rejected PASSED                 [ 33%]
test_shipping.py::test_zero_weight_is_rejected PASSED                    [ 40%]
test_shipping.py::test_bulk_quote[10-1-40.41] PASSED                     [ 46%]
test_shipping.py::test_bulk_quote[1-1-4.04] PASSED                       [ 53%]
test_shipping.py::test_bulk_quote[100-2-539.1] PASSED                    [ 60%]
test_shipping.py::test_delivery_days[IN-3] PASSED                        [ 66%]
test_shipping.py::test_delivery_days[US-6] PASSED                        [ 73%]
test_shipping.py::test_delivery_days[UK-5] PASSED                        [ 80%]
test_shipping.py::test_delivery_days[NZ-10] PASSED                       [ 86%]
test_shipping.py::test_delivery_days[FR-4] SKIPPED (France rate not ...) [ 93%]
test_shipping.py::test_delivery_days[DE-5] XFAIL (DE is not in the t...) [100%]

=========================== short test summary info ============================
SKIPPED [1] test_shipping.py:44: France rate not decided
XFAIL test_shipping.py::test_delivery_days[DE-5] - DE is not in the table, so it takes 10 days
=================== 13 passed, 1 skipped, 1 xfailed in 0.62s ===================
```

Selecting by marker. Each of these shows the collected tests and how many were deselected:

```text
> py -m pytest --collect-only -q -m smoke
test_shipping.py::test_standard_shipping_cost
test_shipping.py::test_express_shipping_cost
test_shipping.py::TestFreeShipping::test_free_from_fifty
test_shipping.py::TestFreeShipping::test_paid_below_fifty
test_shipping.py::test_delivery_days[IN-3]
test_shipping.py::test_delivery_days[US-6]

6/15 tests collected (9 deselected) in 0.01s
```

```text
> py -m pytest --collect-only -q -m "not slow"
test_shipping.py::test_standard_shipping_cost
test_shipping.py::test_express_shipping_cost
test_shipping.py::TestFreeShipping::test_free_from_fifty
test_shipping.py::TestFreeShipping::test_paid_below_fifty
test_shipping.py::test_unknown_method_is_rejected
test_shipping.py::test_zero_weight_is_rejected
test_shipping.py::test_delivery_days[IN-3]
test_shipping.py::test_delivery_days[UK-5]
test_shipping.py::test_delivery_days[NZ-10]
test_shipping.py::test_delivery_days[FR-4]
test_shipping.py::test_delivery_days[DE-5]

11/15 tests collected (4 deselected) in 0.01s
```

```text
> py -m pytest --collect-only -q -m "smoke and not slow"
test_shipping.py::test_standard_shipping_cost
test_shipping.py::test_express_shipping_cost
test_shipping.py::TestFreeShipping::test_free_from_fifty
test_shipping.py::TestFreeShipping::test_paid_below_fifty
test_shipping.py::test_delivery_days[IN-3]

5/15 tests collected (10 deselected) in 0.01s
```

```text
> py -m pytest --collect-only -q -m "smoke and slow"
test_shipping.py::test_delivery_days[US-6]

1/15 tests collected (14 deselected) in 0.01s
```

```text
> py -m pytest --collect-only -q -m "smoke or slow"
test_shipping.py::test_standard_shipping_cost
test_shipping.py::test_express_shipping_cost
test_shipping.py::TestFreeShipping::test_free_from_fifty
test_shipping.py::TestFreeShipping::test_paid_below_fifty
test_shipping.py::test_bulk_quote[10-1-40.41]
test_shipping.py::test_bulk_quote[1-1-4.04]
test_shipping.py::test_bulk_quote[100-2-539.1]
test_shipping.py::test_delivery_days[IN-3]
test_shipping.py::test_delivery_days[US-6]

9/15 tests collected (6 deselected) in 0.01s
```

Running only the quick smoke tests:

```text
> py -m pytest -v -m "smoke and not slow"
============================= test session starts ==============================
collecting ... collected 15 items / 10 deselected / 5 selected

test_shipping.py::test_standard_shipping_cost PASSED                     [ 20%]
test_shipping.py::test_express_shipping_cost PASSED                      [ 40%]
test_shipping.py::TestFreeShipping::test_free_from_fifty PASSED          [ 60%]
test_shipping.py::TestFreeShipping::test_paid_below_fifty PASSED         [ 80%]
test_shipping.py::test_delivery_days[IN-3] PASSED                        [100%]

======================= 5 passed, 10 deselected in 0.01s =======================
```

### Hints

- A custom marker is just `@pytest.mark.<name>`. pytest does not know what it means; you decide, and select with `-m`.
- Register markers in `pytest.ini` (or `pyproject.toml`) under `markers =`, one per line, as `name: description`. The description appears in `py -m pytest --markers`.
- `--strict-markers` turns an unregistered marker (usually a typo such as `@pytest.mark.smok`) into an error. Put it in `addopts` so nobody forgets.
- `-m` takes a Python-like expression: `-m "smoke and not slow"`. Use quotes around it, because of the spaces. On Windows PowerShell and on Ubuntu, double quotes work.
- `pytest.param(value, ..., marks=pytest.mark.slow)` puts a mark on one row of a parametrized test. `marks` takes one mark or a list of marks. You can use `skip` and `xfail` there as well.
- A mark on a class applies to all its test methods. `pytestmark = pytest.mark.smoke` at the top of a file marks every test in the file.
- `-m` and `-k` are different: `-m` selects by marker, `-k` by a part of the test name.

### Acceptance checklist

- [ ] The starter run shows `PytestUnknownMarkWarning`, and you know why.
- [ ] `pytest.ini` registers `smoke` and `slow` with descriptions and sets `addopts = --strict-markers`; the warning is gone.
- [ ] A mark on a class and marks inside `pytest.param(...)` are both used.
- [ ] You ran the five `-m` expressions above and the numbers of selected and deselected tests match what you expected from the table.
- [ ] A deliberate typo such as `@pytest.mark.smok` now makes pytest stop with an error.
- [ ] `shipping.py` was not changed.

---

## T15-E09 - tmp_path, monkeypatch and capsys

**Level:** Medium  |  **Estimated time:** 30 minutes  |  **Practises:** `tmp_path`, testing file reading and writing, `monkeypatch.setenv` and `delenv`, `monkeypatch.setattr`, `capsys`

**Code under test:** `starter/T15_E09/file_report.py` (functions `read_names`, `write_report`, `greet_user`, `fetch_temperature`, `weather_report`)

**Starter test file:** `starter/T15_E09/test_file_report.py` (one test written, three TODOs)

### Problem

Tests must not depend on files lying around, on your environment variables, on the network, or on what the program prints to the screen. pytest has built-in fixtures for all four.

Part A - `tmp_path`. It is a fresh temporary folder (a `pathlib.Path`) for each test. Test:

1. `read_names` strips spaces around names (given).
2. `read_names` skips blank lines and lines starting with `#`.
3. `read_names` of a missing file raises `FileNotFoundError`.
4. `write_report(tmp_path / "out" / "deep" / "report.txt", ["Ravi", "Asha"])` creates the folders, returns 3 (lines written), and the file contains exactly `"Total: 2\n- Asha\n- Ravi\n"` (names sorted).
5. A report written by `write_report` can be read back with `read_names` (comments are not special here: `Total: 2`, `- Asha`, `- Ravi`).

Part B - `monkeypatch` and `capsys` for the environment. `greet_user()` prints a greeting for the user in the environment variable `APP_USER`. `capsys.readouterr()` returns what was printed so far (`.out`, `.err`). Test that with `monkeypatch.setenv("APP_USER", "Asha")` it prints `Hello, Asha!` and that with `monkeypatch.delenv("APP_USER", raising=False)` it prints `Hello, guest!`.

Part C - `monkeypatch.setattr` to replace a function. `weather_report(city)` calls `fetch_temperature(city)`, which always fails with `ConnectionError` here (it pretends to call a web service). Test:

1. Without any patching, `weather_report("Pune")` returns `"Pune: unavailable"` and prints the same line.
2. With `monkeypatch.setattr(file_report, "fetch_temperature", lambda city: temperature)` parametrized for `31.04`, `25` and `24.9`: the result is `Pune: 31.0 C (warm)`, `Pune: 25.0 C (warm)`, `Pune: 24.9 C (cool)`, and the printed output equals the result plus a newline.
3. A test that, without patching, `file_report.fetch_temperature("Pune")` still raises `ConnectionError`: monkeypatch changes are undone after every test.

Patch the name where the code under test looks it up: `weather_report` calls `fetch_temperature` from its own module, so patch `file_report.fetch_temperature`.

### Behaviours to test

| Fixture | What to check |
|---------|---------------|
| `tmp_path` | reading with blanks and comments, missing file, writing creates folders, exact file content |
| `monkeypatch.setenv` / `delenv` | greeting uses the variable, default is `guest` |
| `capsys` | what `print` wrote, compared with `capsys.readouterr().out` |
| `monkeypatch.setattr` | the weather lines for warm, borderline and cool values, no real network use |

### Expected output

The reference solution (12 tests; write at least 10):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 12 items

test_file_report.py::test_read_names_strips_spaces PASSED                [  8%]
test_file_report.py::test_read_names_skips_blank_lines_and_comments PASSED [ 16%]
test_file_report.py::test_read_names_missing_file_raises PASSED          [ 25%]
test_file_report.py::test_write_report_creates_folders_and_sorts_names PASSED [ 33%]
test_file_report.py::test_report_can_be_read_back_with_read_names PASSED [ 41%]
test_file_report.py::test_greet_user_uses_environment_variable PASSED    [ 50%]
test_file_report.py::test_greet_user_defaults_to_guest PASSED            [ 58%]
test_file_report.py::test_weather_report_is_unavailable_without_network PASSED [ 66%]
test_file_report.py::test_weather_report_with_a_replaced_fetch_function[31.04-Pune: 31.0 C (warm)] PASSED [ 75%]
test_file_report.py::test_weather_report_with_a_replaced_fetch_function[25-Pune: 25.0 C (warm)] PASSED [ 83%]
test_file_report.py::test_weather_report_with_a_replaced_fetch_function[24.9-Pune: 24.9 C (cool)] PASSED [ 91%]
test_file_report.py::test_replacement_is_undone_after_each_test PASSED   [100%]

============================== 12 passed in 0.02s ==============================
```

If the default name in the code changes (a deliberately broken copy), the `capsys` check shows exactly what was printed:

```text
> py -m pytest -q --tb=short
......F.....                                                             [100%]
=================================== FAILURES ===================================
______________________ test_greet_user_defaults_to_guest _______________________
test_file_report.py:46: in test_greet_user_defaults_to_guest
    assert capsys.readouterr().out == "Hello, guest!\n"
E   AssertionError: assert 'Hello, friend!\n' == 'Hello, guest!\n'
E
E     - Hello, guest!
E     + Hello, friend!
=========================== short test summary info ============================
FAILED test_file_report.py::test_greet_user_defaults_to_guest - AssertionErro...
1 failed, 11 passed in 0.02s
```

### Hints

- `tmp_path` is a `pathlib.Path`: write with `path.write_text("...", encoding="utf-8")`, read with `path.read_text(encoding="utf-8")`, build paths with `/`.
- pytest deletes old temporary folders for you; you never clean up.
- `monkeypatch.setenv(name, value)` and `monkeypatch.delenv(name, raising=False)` change `os.environ` for one test only. The old state is restored automatically afterwards.
- `capsys.readouterr()` returns a named tuple; `.out` is what was printed to standard output. Calling it again returns only what was printed since the last call.
- `monkeypatch.setattr(module, "name", replacement)` replaces an attribute for one test. A `lambda` is the quickest replacement function.
- Never replace things permanently by assigning `file_report.fetch_temperature = ...` in a test, because it leaks into other tests.

### Acceptance checklist

- [ ] No test writes into the exercise folder; all files are created in `tmp_path`.
- [ ] No test depends on the real value of `APP_USER` or on the network.
- [ ] `capsys` is used to check printed output, `monkeypatch.setenv`, `delenv` and `setattr` are all used.
- [ ] At least 10 tests, all pass, in any order.
- [ ] A broken copy (for example change `"guest"` to `"friend"`) makes at least one of your tests fail.
- [ ] `file_report.py` was not changed.

---

## T15-E10 - Code coverage with pytest-cov

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** `--cov`, `--cov-report=term-missing`, reading the Miss column, `--cov-fail-under`, `--cov-branch`, writing tests to cover missed lines

**Code under test:** `starter/T15_E10/loyalty.py` (functions `points_for_purchase`, `tier_for_points`, `redeem`, `summary`)

**Starter test file:** `starter/T15_E10/test_loyalty.py` (four tests that all pass, but cover only part of the code)

### Problem

Coverage tells you which lines of the code under test ran while your tests ran. It does not prove the tests are good, but a line that never ran is certainly untested. Install with `py -m pip install pytest-cov`.

1. Run `py -m pytest --cov=loyalty --cov-report=term-missing` in the folder. `--cov=loyalty` measures the module `loyalty`; `term-missing` adds the `Missing` column with the line numbers that did not run. Write down the percentage and the missing line ranges.
2. Open `loyalty.py` and match every missing line number to the behaviour it belongs to (error branches, tiers, the `summary` function).
3. Add tests until the coverage is above 90 percent. Aim for tests that check real behaviours (the errors, the tier boundaries 499, 500, 1999, 2000, redeeming with exactly enough points, the summary with and without affordable rewards), not just lines.
4. Add `--cov-fail-under=90` to the command. The run now fails (exit code not zero) when the coverage is below 90, which is how a team keeps the level in a build.
5. Run again with `--cov-branch`, which also checks that both outcomes of each `if` were taken, and compare the numbers.

A `.coverage` data file appears in the folder after each run. It is a result, not source code: do not commit it and delete it when you are done.

### Behaviours to test

| Function | Behaviour |
|----------|-----------|
| `points_for_purchase` | whole units only, tier multipliers 1, 2, 3; negative amount and unknown tier raise `ValueError` |
| `tier_for_points` | bronze below 500, silver below 2000, gold from 2000; negative raises |
| `redeem` | subtracts the cost; exactly enough is allowed; too few raises `ValueError`; unknown reward raises `KeyError` |
| `summary` | no rewards yet, or the most expensive affordable reward |

### Expected output

The starter tests as handed out. Coverage is low, and the `Missing` column shows which lines never ran:

```text
> py -m pytest -q --cov=loyalty --cov-report=term-missing
....                                                                     [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name         Stmts   Miss  Cover   Missing
------------------------------------------
loyalty.py      30     13    57%   11, 13, 20, 22, 24, 31, 34, 40-45
------------------------------------------
TOTAL           30     13    57%
4 passed in 0.02s
```

The same, but failing the run below 90 percent. Note the `FAIL Required test coverage` line; the exit code of the command is not zero:

```text
> py -m pytest -q --cov=loyalty --cov-report=term-missing --cov-fail-under=90
....
ERROR: Coverage failure: total of 57 is less than fail-under=90
                                                                         [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name         Stmts   Miss  Cover   Missing
------------------------------------------
loyalty.py      30     13    57%   11, 13, 20, 22, 24, 31, 34, 40-45
------------------------------------------
TOTAL           30     13    57%
FAIL Required test coverage of 90% not reached. Total coverage: 56.67%
4 passed in 0.02s
```

The reference solution (17 tests; write enough to pass 90 percent):

```text
> py -m pytest -q --cov=loyalty --cov-report=term-missing --cov-fail-under=90
.................                                                        [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name         Stmts   Miss  Cover   Missing
------------------------------------------
loyalty.py      30      0   100%
------------------------------------------
TOTAL           30      0   100%
Required test coverage of 90% reached. Total coverage: 100.00%
17 passed in 0.03s
```

With branch coverage:

```text
> py -m pytest -q --cov=loyalty --cov-branch --cov-report=term-missing
.................                                                        [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name         Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------
loyalty.py      30      0     16      0   100%
--------------------------------------------------------
TOTAL           30      0     16      0   100%
17 passed in 0.04s
```

### Hints

- `--cov=loyalty` takes the module (or package) name, not a file name. Without it, no coverage is measured.
- `Stmts` is the number of statements, `Miss` how many did not run, `Cover` the percentage, `Missing` the line numbers (`23-24, 31` means lines 23 to 24 and 31).
- Look at the missing lines first: most are `raise` lines of error cases. Each one needs a test with `pytest.raises`.
- 100 percent is not the goal. A test that only calls the code and asserts nothing raises coverage but proves nothing.
- `--cov-report=html` writes a folder `htmlcov/` with a page where missed lines are highlighted. Delete the folder afterwards.
- The Windows command is the same; coverage files and folders are created in the current folder.

### Acceptance checklist

- [ ] You wrote down the starting percentage and the missing lines, and know which behaviour each missing line is.
- [ ] `py -m pytest --cov=loyalty --cov-report=term-missing --cov-fail-under=90` passes.
- [ ] The new tests assert real behaviour (return values and exceptions), not just run the code.
- [ ] You ran the report with `--cov-branch` and can explain why the number can be lower.
- [ ] The `.coverage` file (and `htmlcov/` if you made it) was deleted afterwards.
- [ ] `loyalty.py` was not changed.

---

## T15-E11 - Challenge: test a shopping cart end to end

**Level:** Hard (Challenge)  |  **Estimated time:** 30 minutes  |  **Practises:** designing a test suite from rules, shared fixtures in `conftest.py`, classes of tests, parametrize with `pytest.param`, exceptions, floating point money, coverage above 90 percent

**Code under test:** `starter/T15_E11/cart.py` (classes `Product`, `Cart`, exception `EmptyCartError`; the rules are in the docstring at the top of the file)

**Starter test file:** `starter/T15_E11/test_cart.py` (empty except for the imports)

### Problem

Write a complete test suite for the shopping cart. Read the rules in the docstring of `cart.py` first. Put shared fixtures in `conftest.py`:

- `tea` = `Product("T1", "Tea", 4.50)`, `book` = `Product("B1", "Book", 12.00)`, `lamp` = `Product("L1", "Lamp", 35.00)`;
- `cart`: an empty `Cart`;
- `filled_cart`: the `cart` with two teas and one book (subtotal 21.00).

Group the tests in classes (`TestProduct`, `TestEmptyCart`, `TestAddAndRemove`, `TestSubtotal`, `TestCoupons`, `TestShippingAndTax`, `TestTotal`, `TestCheckout`). Cover every rule:

- Product: a negative price raises `ValueError`; a product is frozen (assigning to `price` raises `dataclasses.FrozenInstanceError`).
- Empty cart: empty, no items, quantity 0, subtotal / shipping / total all 0, checkout raises `EmptyCartError`.
- Add and remove: add one; adding the same product twice adds the quantities; quantity 0 and -1 are rejected (parametrize); remove some, remove all (`None`), removing more than there is removes the product, unknown SKU raises `KeyError`, removing quantity 0 raises `ValueError` and changes nothing.
- Subtotal: 21.00 for the filled cart; three items at 0.10 give exactly `0.3` (rounding).
- Coupons: `SAVE10` takes 10 percent (2.10 off 21.00); the code is trimmed and case-insensitive; `FIVER` takes 5.00 off; `FIVER` is refused below a subtotal of 20.00 and accepted at exactly 20.00; unknown code raises `ValueError`; a second coupon is refused and the first stays; no coupon means no discount.
- Shipping and tax: shipping 4.99 below 50, free at exactly 50.00; the free-shipping test uses the price AFTER the coupon (55.00 with `SAVE10` is 49.50, so shipping is charged); tax is 8 percent of the price after the coupon (1.68, and 1.51 with `SAVE10`).
- Totals (parametrize with `pytest.param(..., id=...)`): filled cart is 27.67 without a coupon, 25.40 with `SAVE10`, 22.27 with `FIVER`; two lamps (70.00) cost 75.60 with free shipping. Compare money with `pytest.approx`.
- Checkout: the receipt dictionary has `items`, `subtotal`, `discount`, `tax`, `shipping` and `total` (check the whole dictionary for the `SAVE10` case); after checkout the cart is empty and the coupon is gone; the cart can be used again.

Finally run `py -m pytest --cov=cart --cov-report=term-missing --cov-fail-under=90` and make sure the coverage is above 90 percent.

### Behaviours to test

See the list above; the table gives the numbers to expect.

| Case | Expected |
|------|----------|
| filled cart, no coupon | subtotal 21.00, tax 1.68, shipping 4.99, total 27.67 |
| filled cart, `SAVE10` | discount 2.10, tax 1.51, total 25.40 |
| filled cart, `FIVER` | discount 5.00, total 22.27 |
| 2 lamps | subtotal 70.00, shipping 0.00, total 75.60 |
| 55.00 item with `SAVE10` | price after coupon 49.50, shipping 4.99 |

### Expected output

The reference solution with coverage (36 tests; write at least 28):

```text
> py -m pytest -q --cov=cart --cov-report=term-missing --cov-fail-under=90
....................................                                     [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name      Stmts   Miss  Cover   Missing
---------------------------------------
cart.py      75      0   100%
---------------------------------------
TOTAL        75      0   100%
Required test coverage of 90% reached. Total coverage: 100.00%
36 passed in 0.08s
```

The tests for the totals:

```text
> py -m pytest -v -k TestTotal
============================= test session starts ==============================
collecting ... collected 36 items / 32 deselected / 4 selected

test_cart.py::TestTotal::test_total_of_the_filled_cart[no-coupon] PASSED [ 25%]
test_cart.py::TestTotal::test_total_of_the_filled_cart[save10] PASSED    [ 50%]
test_cart.py::TestTotal::test_total_of_the_filled_cart[fiver] PASSED     [ 75%]
test_cart.py::TestTotal::test_total_with_free_shipping PASSED            [100%]

======================= 4 passed, 32 deselected in 0.02s =======================
```

Your suite must be able to catch real bugs. With a deliberately broken copy in which a second coupon is allowed, the reference suite fails like this:

```text
> py -m pytest -q --tb=short
......................F.............                                     [100%]
=================================== FAILURES ===================================
__________________ TestCoupons.test_only_one_coupon_at_a_time __________________
test_cart.py:114: in test_only_one_coupon_at_a_time
    with pytest.raises(ValueError, match="already applied"):
E   Failed: DID NOT RAISE ValueError
=========================== short test summary info ============================
FAILED test_cart.py::TestCoupons::test_only_one_coupon_at_a_time - Failed: DI...
1 failed, 35 passed in 0.04s
```

And with a copy in which tax is charged before the coupon is taken off:

```text
> py -m pytest -q --tb=line
............................F.FF.F..                                     [100%]
=================================== FAILURES ===================================
E   assert 1.68 == 1.51
./test_cart.py:142: assert 1.68 == 1.51
E   assert 25.57 == 25.4 ± 2.5e-05

      comparison failed
      Obtained: 25.57
      Expected: 25.4 ± 2.5e-05
./test_cart.py:157: assert 25.57 == 25.4 ± 2.5e-05
E   assert 22.67 == 22.27 ± 2.2e-05

      comparison failed
      Obtained: 22.67
      Expected: 22.27 ± 2.2e-05
./test_cart.py:157: assert 22.67 == 22.27 ± 2.2e-05
E   AssertionError: assert {'items': 3, ...x': 1.68, ...} == {'items': 3, ...x': 1.51, ...}

      Omitting 4 identical items, use -vv to show
      Differing items:
      {'tax': 1.68} != {'tax': 1.51}
      {'total': 25.57} != {'total': 25.4}
      Use -v to get more diff
./test_cart.py:168: AssertionError: assert {'items': 3, ...x': 1.68, ...} == {'items': 3, ...x': 1.51, ...}
=========================== short test summary info ============================
FAILED test_cart.py::TestShippingAndTax::test_tax_is_charged_after_the_coupon
FAILED test_cart.py::TestTotal::test_total_of_the_filled_cart[save10] - asser...
FAILED test_cart.py::TestTotal::test_total_of_the_filled_cart[fiver] - assert...
FAILED test_cart.py::TestCheckout::test_receipt_has_every_figure - AssertionE...
4 failed, 32 passed in 0.03s
```

### Hints

- Start with the fixtures, then one class at a time, and run after each class.
- The test for "shipping uses the price after the coupon" needs a subtotal over 50 that falls under 50 after `SAVE10`: 55.00 gives 49.50.
- For floating point money use `pytest.approx` (or compare rounded values the code itself rounds, as it rounds to 2 places).
- A test of an exception should also check that nothing changed (`cart.coupon is None`, quantity unchanged).
- Look at the `Missing` column after your first run: it shows the rules you forgot.
- Try small changes in `cart.py` on a copy (for example `>=` to `>` in the shipping rule) and check that at least one test fails. This is called mutation testing by hand.

### Acceptance checklist

- [ ] `conftest.py` has the six fixtures; no test builds products or carts by hand without a reason.
- [ ] At least 28 tests in at least six classes, all pass.
- [ ] Parametrize with `pytest.param(..., id=...)` is used at least once.
- [ ] `--cov=cart --cov-fail-under=90` passes.
- [ ] Each of these changes to a copy of `cart.py` makes at least one test fail: second coupon allowed, `>=` changed to `>` in the free shipping rule, tax charged before the coupon, `checkout()` not emptying the cart.
- [ ] `cart.py` was not changed.

---

## T15-E12 - Challenge: test a JSON-reading function with fixtures and parametrize

**Level:** Hard (Challenge)  |  **Estimated time:** 30 minutes  |  **Practises:** `tmp_path`, a factory fixture (a fixture that returns a function), fixtures that build on fixtures, `pytest.param` with `id`, `pytest.raises(..., match=...)`, testing error messages, coverage

**Code under test:** `starter/T15_E12/inventory_reader.py` (functions `load_products`, `total_value`, `load_summary`; the file format is in the docstring at the top)

**Sample data:** `starter/T15_E12/sample_inventory.json` (to try the code by hand; the tests should create their own files in `tmp_path`)

**Starter test file:** `starter/T15_E12/test_inventory_reader.py` (empty except for the imports)

### Problem

`load_products(path)` reads a JSON inventory file and returns a list of clean records. Read the code to see the rules, then write the tests. Do not read `sample_inventory.json` from the tests: create small files in `tmp_path` so that each test controls its own data.

Fixtures in `conftest.py`:

1. `write_json`: uses `tmp_path` and returns a function `_write(data, name="inventory.json")` that dumps a Python object as JSON into `tmp_path` and returns the path (a factory fixture).
2. `write_text`: the same for raw text (needed for broken JSON).
3. `valid_file`: uses `write_json` to write four products: Pen (1.5, qty 100), Notebook (price as the string `"3.25"`, qty 40), Stapler (8, qty 5) and Ruler (0.9, no qty).

Tests (group them in classes `TestLoadProducts`, `TestBadInput`, `TestTotals`):

- Valid file: the first record is `{"name": "Pen", "price": 1.5, "qty": 100}` and there are four; the string price becomes the float `3.25`; a missing `qty` becomes 0; names are stripped of spaces; an empty list `[]` gives `[]`; a missing file raises `FileNotFoundError`.
- Broken JSON (`'{"name": "Pen", '`) raises `ValueError` matching `invalid JSON`.
- Parametrize with `pytest.param(..., id=...)`: the top-level document must be a list. Try an object, a string, a number and `null`; each raises `ValueError` matching `top level must be a list`.
- Parametrize the bad records (use `pytest.param(records, message, id=...)`, ten cases) and check the exact position-based message with `match=`:

| id | record(s) | message contains |
|----|-----------|------------------|
| no-name | `{"price": 1}` | `record 1: missing key 'name'` |
| no-price | `{"name": "Pen"}` | `record 1: missing key 'price'` |
| blank-name | second record has name `" "` | `record 2: name is empty` |
| text-price | price `"free"` | `record 1: price is not a number` |
| null-price | price `null` | `record 1: price is not a number` |
| negative-price | price `-1` | `record 1: price cannot be negative` |
| fractional-qty | qty `2.5` | `record 1: qty must be a whole number` |
| negative-qty | qty `-3` | `record 1: qty must be a whole number` |
| boolean-qty | qty `true` | `record 1: qty must be a whole number` |
| record-not-object | the record is the string `"Pen"` | `record 1: must be an object` |

- Totals: `total_value(load_products(valid_file))` is 320 (150 + 130 + 40); `total_value([])` is 0; `load_summary(valid_file)` is `{"count": 4, "units": 145, "value": 320.0}`; `load_summary` of a bad document raises `ValueError`.

Run with `py -m pytest --cov=inventory_reader --cov-report=term-missing --cov-fail-under=90`.

### Behaviours to test

See the lists and the table above. The code has nine different error messages; a good suite triggers each of them.

### Expected output

The reference solution (25 tests; the parametrized cases count as separate tests; write at least 20):

```text
> py -m pytest -v
============================= test session starts ==============================
collecting ... collected 25 items

test_inventory_reader.py::TestLoadProducts::test_valid_file_gives_clean_records PASSED [  4%]
test_inventory_reader.py::TestLoadProducts::test_numeric_string_price_becomes_a_float PASSED [  8%]
test_inventory_reader.py::TestLoadProducts::test_qty_defaults_to_zero PASSED [ 12%]
test_inventory_reader.py::TestLoadProducts::test_names_are_stripped PASSED [ 16%]
test_inventory_reader.py::TestLoadProducts::test_empty_list_is_valid PASSED [ 20%]
test_inventory_reader.py::TestLoadProducts::test_missing_file_raises_file_not_found PASSED [ 24%]
test_inventory_reader.py::TestBadInput::test_broken_json_raises_value_error PASSED [ 28%]
test_inventory_reader.py::TestBadInput::test_top_level_must_be_a_list[object-not-list] PASSED [ 32%]
test_inventory_reader.py::TestBadInput::test_top_level_must_be_a_list[string-not-list] PASSED [ 36%]
test_inventory_reader.py::TestBadInput::test_top_level_must_be_a_list[number-not-list] PASSED [ 40%]
test_inventory_reader.py::TestBadInput::test_top_level_must_be_a_list[null-not-list] PASSED [ 44%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[no-name] PASSED [ 48%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[no-price] PASSED [ 52%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[blank-name] PASSED [ 56%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[text-price] PASSED [ 60%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[null-price] PASSED [ 64%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[negative-price] PASSED [ 68%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[fractional-qty] PASSED [ 72%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[negative-qty] PASSED [ 76%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[boolean-qty] PASSED [ 80%]
test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[record-not-object] PASSED [ 84%]
test_inventory_reader.py::TestTotals::test_total_value_of_the_valid_file PASSED [ 88%]
test_inventory_reader.py::TestTotals::test_total_value_of_nothing_is_zero PASSED [ 92%]
test_inventory_reader.py::TestTotals::test_summary PASSED                [ 96%]
test_inventory_reader.py::TestTotals::test_summary_of_a_bad_file_raises PASSED [100%]

============================== 25 passed in 0.03s ==============================
```

With coverage:

```text
> py -m pytest -q --cov=inventory_reader --cov-report=term-missing --cov-fail-under=90
.........................                                                [100%]
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.3-final-0 ________________

Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
inventory_reader.py      38      0   100%
---------------------------------------------------
TOTAL                    38      0   100%
Required test coverage of 90% reached. Total coverage: 100.00%
25 passed in 0.07s
```

With a deliberately broken copy in which the check for missing keys is removed, the matching rows fail and the others pass:

```text
> py -m pytest -q --tb=short
...........FF............                                                [100%]
=================================== FAILURES ===================================
_______ TestBadInput.test_bad_records_are_reported_by_position[no-name] ________
test_inventory_reader.py:94: in test_bad_records_are_reported_by_position
    load_products(write_json(records))
inventory_reader.py:23: in load_products
    products.append(_clean_record(index, record))
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
inventory_reader.py:33: in _clean_record
    name = str(record["name"]).strip()
               ^^^^^^^^^^^^^^
E   KeyError: 'name'
_______ TestBadInput.test_bad_records_are_reported_by_position[no-price] _______
test_inventory_reader.py:94: in test_bad_records_are_reported_by_position
    load_products(write_json(records))
inventory_reader.py:23: in load_products
    products.append(_clean_record(index, record))
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
inventory_reader.py:37: in _clean_record
    price = float(record["price"])
                  ^^^^^^^^^^^^^^^
E   KeyError: 'price'
=========================== short test summary info ============================
FAILED test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[no-name]
FAILED test_inventory_reader.py::TestBadInput::test_bad_records_are_reported_by_position[no-price]
2 failed, 23 passed in 0.04s
```

### Hints

- A factory fixture returns a function, so a test can create several files with different content: `path = write_json([...])`.
- `json.dumps(data)` turns a Python object into JSON text. For broken JSON write the text yourself with `write_text`.
- `match` is a regular expression that is searched in the message. The messages here contain only letters, digits, spaces, `:` and `'`, which are safe in a regular expression.
- Give every `pytest.param` an `id`; the failing row is then easy to find (`test_bad_records_are_reported_by_position[no-price]`).
- To run only one row: `py -m pytest -k "no-price"`.
- Put the bad cases in tables (lists of `pytest.param`) and keep the test function itself short.

### Acceptance checklist

- [ ] `conftest.py` has `write_json` (a factory fixture), `write_text` and `valid_file`.
- [ ] No test reads `sample_inventory.json`; all files are created in `tmp_path`.
- [ ] Parametrize with `pytest.param(..., id=...)` is used for the top-level types and for the ten bad records.
- [ ] At least 20 tests, all pass; coverage of `inventory_reader` is above 90 percent.
- [ ] Each of these changes to a copy of the code makes at least one test fail: negative prices accepted, missing keys not checked, broken JSON swallowed, `True` accepted as a quantity, `qty` ignored in `total_value`.
- [ ] `inventory_reader.py` was not changed.
