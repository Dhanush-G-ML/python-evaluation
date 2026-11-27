# T14-E12 - Challenge: a small shop app with per-module loggers and dictConfig
#
# Build a package named `shop` (a folder `shop/` with `__init__.py`) with these modules. Each module that logs creates its logger with `logger = logging.getLogger(__name__)`, so the logger names are `shop.inventory`, `shop.payments` and `shop.orders`.
#
# - `shop/inventory.py`: a `STOCK` dict, `load_stock()` (widget 10, gadget 3, gizmo 3, doohickey 0; logs `DEBUG` `stock loaded: <dict>`), `reserve(sku, qty)` and `release(sku, qty)`. `reserve` logs `DEBUG` `checking stock for <sku> x<qty>`, raises `UnknownProduct(sku)` for an unknown product and `OutOfStock("<sku>: wanted <qty>, have <n>")` when there is not enough, otherwise lowers the stock and logs `INFO` `reserved <qty> x <sku>`; when one or no items are left it also logs `WARNING` `low stock for <sku>: <n> left`. `release` adds the stock back and logs `DEBUG` `released <qty> x <sku>`.
# - `shop/payments.py`: `charge(card, amount)` logs `DEBUG` `contacting the gateway for card <card>`, `INFO` `charging <amount, two decimals> to card <card>`, raises `PaymentDeclined("amount <amount> is over the limit of <limit>")` (two decimals, limit 1000) or logs `INFO` `payment accepted`.
# - `shop/orders.py`: `place_order(order)` logs `INFO` `order <id> received from <customer>`, reserves every item, charges the card, and on `OutOfStock`, `UnknownProduct` or `PaymentDeclined` releases what was reserved, logs `ERROR` `order <id> failed: <exception>` with `exc_info=True` and returns `False`. On success it logs `INFO` `order <id> completed` and returns `True`.
# - `shop/formatting.py`: a `MaskFilter` (replaces card numbers of 12 to 16 digits with `*` characters and the last four digits), a `CompactFormatter` (takes `fmt` and `show_exception`; an exception is shown as `    raised in <function>(): <Type>: <message>`, or not at all when `show_exception` is false) and a `JsonFormatter` (as in T14-E08).
# - `shop/config.py`: `build_config(log_dir)` returns a **configuration dictionary** for `logging.config.dictConfig`, and `setup_logging(log_dir)` creates the folder and applies it.
# - `shop/app.py`: `run_orders(path)` loads the stock, reads the JSON orders, places each one, and also makes two calls on a logger named `thirdparty`: `info("this INFO line is hidden by the root level")` and `warning("a library warns on the root logger")`. It returns a dict from order id to the result.
#
# The configuration (use `"version": 1` and `"disable_existing_loggers": False`) must contain:
#
# - Formatter `brief`: `CompactFormatter`, `%(levelname)-7s %(name)s: %(message)s`, `show_exception` false.
# - Formatter `detailed`: `CompactFormatter`, `%(levelname)-7s %(name)s.%(funcName)s: %(message)s`.
# - Formatter `json`: `JsonFormatter`.
# - Filter `mask`: `MaskFilter`.
# - Handler `console`: `StreamHandler` on `ext://sys.stdout`, level `INFO`, formatter `brief`, filter `mask`.
# - Handler `file`: `FileHandler` for `shop.log` (mode `w`), level `DEBUG`, formatter `detailed`, filter `mask`.
# - Handler `errors`: `RotatingFileHandler` for `errors.jsonl` (mode `w`, 10000 bytes, 2 backups), level `ERROR`, formatter `json`, filter `mask`.
# - Logger `shop`: level `DEBUG`, handlers `console`, `file` and `errors`, `propagate` false.
# - Logger `shop.payments`: level `INFO`, no handlers of its own.
# - Root logger: level `WARNING`, handler `console`.
#
# The main program writes the logs into `output/shop`, runs the orders in `data/shop_orders.json`, and prints: `--- console ---` and then everything the console handler shows; `--- logger table ---` with name, own level, effective level, `propagate` and the handler class names of the four loggers `shop`, `shop.inventory`, `shop.payments`, `shop.orders`; then (after logging is shut down) the content of `shop.log`, the content of `errors.jsonl` and `Completed <n> of <m> orders: <ids>`.
