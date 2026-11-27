# T15-E05 - Fixtures: setup, yield teardown and scope
#
# A `Bank` opens accounts (`open_account(owner, deposit=0)` returns 1, 2, 3, ...), keeps balances (`balance`, `deposit`, `account_count`, `total_deposits`) and can be closed (`close()`). Every `Bank` registers itself in the class list `Bank.open_banks` and removes itself when it is closed, so a test that forgets to close its bank leaves it in that list.
#
# Build these fixtures in `test_bank.py` and use them:
#
# 1. `bank`: creates `Bank("Test Bank")`, hands it to the test with `yield`, and closes it afterwards (the code after `yield` is the teardown and runs even when the test fails). Rewrite the first test to use it.
# 2. `bank_with_two_accounts`: uses the `bank` fixture, opens an account for Asha with 100 and one for Ravi with 50, and returns `(bank, first_number, second_number)`.
# 3. `no_open_banks_left`: a module-scoped, autouse fixture that does nothing before the tests and, after the last test of the file, asserts that `Bank.open_banks == []`. It is a leak check for your other fixtures.
# 4. `shared_bank`: a module-scoped fixture (one `Bank("Shared Bank")` for all tests of the file, closed at the end).
#
# Write the tests:
#
# - a new bank has no accounts; account numbers start at 1 and go up; a negative opening deposit raises `ValueError`;
# - `deposit` changes one balance and not the other; `total_deposits` adds all accounts (use `bank_with_two_accounts`);
# - a closed bank raises `RuntimeError` (message contains `closed`) when you open an account;
# - scope demonstration: one test that opens an account in `shared_bank` and asserts the count is 1, and a second test (defined after it) that asserts the count is still 1, because with module scope both tests received the same bank.
#
# Then run the tests with `--setup-show` and read when each fixture is set up and torn down.
#
# Behaviours to test
#
# | Fixture or area | What to check |
# |-----------------|---------------|
# | `bank` (function scope) | each test gets a fresh, empty bank; it is closed afterwards |
# | `bank_with_two_accounts` | numbers 1 and 2, balances 100 and 50, total 150 |
# | `no_open_banks_left` | after the module, no bank is left open |
# | `shared_bank` (module scope) | the second test sees the account the first test opened |
# | `Bank` | closed bank rejects `open_account`, negative deposit rejected |
