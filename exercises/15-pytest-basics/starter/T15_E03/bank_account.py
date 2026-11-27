"""A simple bank account. This is the code under test: do not change it."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self._history = []

    @property
    def balance(self):
        return self._balance

    @property
    def history(self):
        """A copy of the list of (kind, amount) entries, oldest first."""
        return list(self._history)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
        self._history.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"cannot withdraw {amount}: balance is {self._balance}"
            )
        self._balance -= amount
        self._history.append(("withdraw", amount))
        return self._balance

    def transfer(self, other, amount):
        """Move money to another account. Nothing changes if it fails."""
        self.withdraw(amount)
        other.deposit(amount)
