# T13-E06 Bank account simulator with exceptions and decorators
#
# Simulate a bank that runs a script of commands, one per line, from a file or from stdin. Lines
# starting with `#` are comments. The commands are `open`, `deposit`, `withdraw`, `transfer`,
# `interest`, `freeze`, `unfreeze`, `statement` and `summary`; see the sample file
# `data/bank_commands.txt`. The bank has these rules:
#
# - Account types are `basic`, `checking` and `savings`. A checking account may go up to 100 below
#   zero. A savings account allows 3 withdrawals, and transfers out count as withdrawals.
# - Write these decorators: `@validate_amount` (turns the amount into a positive `Decimal` or
#   raises `InvalidAmount`), `@require_active` (raises `AccountFrozen` for a frozen account), and
#   `@record(kind)` (adds `(kind, amount, balance)` to the history only when the operation succeeds).
# - Write these exceptions, all subclasses of `BankError`: `InvalidAmount`, `InsufficientFunds`,
#   `AccountFrozen`, `LimitExceeded` and `UnknownAccount`.
# - A transfer is all or nothing. If the deposit fails, undo the withdrawal.
# - A failing line prints its line number and the exception name, and the script carries on.
#
# Suggested modules: `exceptions.py`, `decorators.py`, `accounts.py` (`Account`, `CheckingAccount`,
# `SavingsAccount`, `Bank`), `cli.py`.
