import pytest

from bank import Bank


def test_new_bank_has_no_accounts():
    bank = Bank("Local Bank")
    assert bank.account_count() == 0
    bank.close()

# TODO 1: write a fixture called `bank` that creates a Bank("Test Bank"),
#         yields it, and closes it afterwards (teardown). Rewrite the test
#         above to use the fixture and remove the manual close().
# TODO 2: write a fixture called `bank_with_two_accounts` that builds on `bank`.
# TODO 3: write the module-scoped, autouse "leak check" fixture (see exercises.md).
# TODO 4: add the two scope tests (see exercises.md).
