# T04-E06 - Custom exceptions for a bank account
#
# Define these exceptions:
#
# - `BankError(Exception)` - base class.
# - `InvalidAmountError(BankError)` and `AccountFrozenError(BankError)`.
# - `InsufficientFundsError(BankError)` - created with `(balance, amount)`, stores attributes `balance`, `amount` and `shortfall`, and has the message `Insufficient funds: balance 70.00, requested 100.00 (short by 30.00)`.
#
# Write a class `Account(owner, balance=0)` with a `frozen` flag and methods `deposit(amount)` and `withdraw(amount)`. A frozen account raises `AccountFrozenError` (message `Account of <owner> is frozen`); an amount of zero or less raises `InvalidAmountError` (message `Amount must be positive, got <amount>`); withdrawing more than the balance raises `InsufficientFundsError`. A failed operation must not change the balance.
#
# Run the script of operations below on `Account("Asha")`. Catch `InsufficientFundsError` separately (also print its `shortfall` attribute) and everything else with one `except BankError`.
