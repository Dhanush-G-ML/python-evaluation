# T10-E05: Adapter: payment gateways
#
# **Pattern: Adapter.** Your shop code expects every payment provider to look like this:
#
# ```python
# class PaymentProcessor(ABC):
#     """The interface our shop code expects."""
#
#     @abstractmethod
#     def pay(self, amount_cents, currency="EUR"):
#         """Return a receipt string such as 'PAID FP-1001' or raise PaymentDeclined."""
# ```
#
# Two third-party clients cannot be changed and have incompatible methods:
#
# ```python
# class FastPayClient:
#     def __init__(self):
#         self._next = 1001
#
#     def charge(self, amount, card_token):
#         ref = f"FP-{self._next}"
#         self._next += 1
#         status = "approved" if amount <= 1000 else "declined"
#         return {"status": status, "id": ref}
#
#
# class GlobalPayClient:
#     def __init__(self):
#         self._next = 2001
#
#     def send(self, amount_cents, currency):
#         ref = f"GP-{self._next}"
#         self._next += 1
#         return (0 if amount_cents <= 500000 else 5, ref)
# ```
#
# Write `FastPayAdapter(client, card_token)` and `GlobalPayAdapter(client)`; both must be `PaymentProcessor` subclasses.
#
# - `FastPayAdapter.pay` converts cents to a decimal amount, calls `charge`, and returns `PAID <id>` when the status is
#   `"approved"`. Otherwise it raises `PaymentDeclined(f"FastPay declined {amount}")` where `amount` is the decimal
#   amount (for example `1500.0`).
# - `GlobalPayAdapter.pay` calls `send`; a code of `0` means success and returns `PAID <reference>`. Any other code
#   raises `PaymentDeclined(f"GlobalPay error code {code}")`.
#
# Also write the exception `PaymentDeclined(Exception)` and the interface above exactly as shown.
