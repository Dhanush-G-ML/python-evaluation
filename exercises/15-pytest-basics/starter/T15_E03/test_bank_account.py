import pytest

from bank_account import BankAccount, InsufficientFundsError


class TestBankAccount:
    def test_new_account_has_opening_balance(self):
        account = BankAccount("Asha", 100)
        assert account.owner == "Asha"
        assert account.balance == 100

    # TODO: new account without a balance starts at 0 and has an empty history
    # TODO: deposit and withdraw change the balance and are recorded in history
    # TODO: the history list you get back is a copy (changing it changes nothing)
    # TODO: a failed withdrawal raises InsufficientFundsError and changes nothing
    # TODO: bad amounts (0, negative) raise ValueError
    # TODO: transfer moves money; a failed transfer changes neither account
