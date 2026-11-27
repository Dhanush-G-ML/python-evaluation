"""A small bank that keeps many accounts. This is the code under test: do not change it."""


class Bank:
    open_banks = []

    def __init__(self, name):
        self.name = name
        self.closed = False
        self._balances = {}
        self._next_number = 1
        Bank.open_banks.append(self)

    def open_account(self, owner, deposit=0):
        """Open an account and return its account number (1, 2, 3, ...)."""
        if self.closed:
            raise RuntimeError("bank is closed")
        if deposit < 0:
            raise ValueError("deposit cannot be negative")
        number = self._next_number
        self._next_number += 1
        self._balances[number] = {"owner": owner, "balance": deposit}
        return number

    def balance(self, number):
        return self._balances[number]["balance"]

    def deposit(self, number, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balances[number]["balance"] += amount

    def account_count(self):
        return len(self._balances)

    def total_deposits(self):
        return sum(item["balance"] for item in self._balances.values())

    def close(self):
        """Close the bank. Closing twice is harmless."""
        if not self.closed:
            self.closed = True
            Bank.open_banks.remove(self)
