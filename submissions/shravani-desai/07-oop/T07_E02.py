# T07-E02: Bank account with validation
#
# Write a custom exception `InsufficientFundsError` that inherits from `ValueError`, and a class `BankAccount`
# created with `owner` and an optional starting `balance` (default `0`).
#
# - `deposit(amount)` adds to the balance. If `amount <= 0` raise `ValueError("Deposit must be positive")`.
# - `withdraw(amount)` subtracts from the balance. If `amount <= 0` raise `ValueError("Withdrawal must be positive")`.
#   If `amount` is more than the balance raise `InsufficientFundsError(f"Cannot withdraw {amount}, balance is {balance}")`.
# - Every successful operation is recorded in `self.history` as a tuple `("deposit", amount)` or `("withdraw", amount)`.
# - `statement()` returns a multi-line string: a header `Statement for <owner>`, one line per history entry
#   (kind left-aligned in 10 characters, amount right-aligned in 8 characters), and a final `Balance: <n>` line.
