# T07-E07: Inventory records with dataclasses
#
# Use the `dataclasses` module.
#
# 1. `Product` with fields `name: str`, `price: float`, `quantity: int = 0` and `tags: list` (default must be a
#    new empty list per object). Use `__post_init__` to raise `ValueError("price cannot be negative")`. Add a
#    method `total_value()` returning `round(price * quantity, 2)`.
# 2. `Version` with `major`, `minor=0`, `patch=0`. It must be **frozen** (immutable) and **orderable**, and
#    `str(v)` returns `"1.2.3"`.
#
# The driver also uses `dataclasses.asdict` and `dataclasses.replace`, so import them too.
