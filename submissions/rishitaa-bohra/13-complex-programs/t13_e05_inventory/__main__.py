# T13-E05 Text-based inventory with classes and file persistence
#
# Build a menu-driven inventory manager for a small shop. It loads from `data/inventory.json` and
# saves back to the same file. The menu has these options:
#
# 1. List: a table of SKU, name, quantity, price and value, with `reorder` shown next to items at
#    or below their reorder level, followed by the total stock value.
# 2. Add product. The SKU is stored in uppercase and must be unique.
# 3. Restock.
# 4. Sell. You cannot sell more than you have in stock.
# 5. Low stock report.
# 6. Save and quit.
#
# Use custom exceptions (`InventoryError` and its subclasses `UnknownProduct`, `DuplicateProduct`
# and `OutOfStock`) and keep a movement history (`add`, `restock` and `sell` entries) in the file.
#
# Suggested modules: `models.py` (`Product`, `Inventory`, exceptions), `storage.py`, `cli.py`.
