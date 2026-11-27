# T15-E03 - Testing a class and its state
#
# A `BankAccount(owner, balance=0)` has a `balance` and a `history` (a list of `("deposit", amount)` and `("withdraw", amount)` entries). `deposit` and `withdraw` return the new balance and raise `ValueError` for amounts of zero or less. `withdraw` raises `InsufficientFundsError` when the amount is more than the balance. `transfer(other, amount)` moves money to another account. A failed operation must change nothing.
#
# Write the tests. Every test creates its own account(s) inside the test, so no test depends on another. Group them in classes whose names start with `Test` (for example `TestOpening`, `TestDepositAndWithdraw`, `TestFailedOperationsChangeNothing`, `TestTransfer`). Test:
#
# 1. A new account keeps the owner and the opening balance; without a balance it starts at 0 with an empty history; a negative opening balance raises `ValueError`.
# 2. `deposit(50)` on a balance of 100 returns and shows 150; `withdraw(30)` returns and shows 70; withdrawing the whole balance is allowed.
# 3. The history lists every successful operation, oldest first.
# 4. Amounts of 0 and -10 raise `ValueError` for both deposit and withdraw, and the balance is unchanged.
# 5. An overdraft raises `InsufficientFundsError` (check the message with `match="balance is 100"`), and neither balance nor history changed.
# 6. The `history` you get back is a copy: appending to it does not change the account.
# 7. A transfer changes both balances; a failed transfer changes neither account; two accounts never share state.
#
# Behaviours to test
#
# | Area | Behaviour |
# |------|-----------|
# | Opening | owner, balance, defaults, negative balance rejected |
# | Deposit / withdraw | new balance returned and stored, whole balance can be withdrawn |
# | History | successful operations recorded in order, copy returned |
# | Errors | bad amounts, overdraft: exception raised, state unchanged |
# | Transfer | both balances change, failed transfer changes nothing |
# | Independence | separate accounts do not share state |
