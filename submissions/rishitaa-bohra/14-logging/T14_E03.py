# T14-E03 - Formatters
#
# To get the same output every time, the program builds its own log records instead of logging live. The helper below is given; copy it into your program:
#
# ```python
# import logging
# import time
#
# CREATED = 1_700_000_000.5  # 2023-11-14 22:13:20.5 UTC
#
#
# def sample_records():
#     base = {
#         "name": "billing", "pathname": "/app/billing.py", "filename": "billing.py",
#         "module": "billing", "funcName": "send_invoice", "lineno": 42,
#         "created": CREATED, "msecs": 500.0,
#     }
#     specs = [
#         (logging.INFO, "Invoice %s sent to %s", ("A-17", "ana@example.com")),
#         (logging.WARNING, "Invoice %s is %d days late", ("A-12", 9)),
#         (logging.ERROR, "Could not send invoice %s", ("A-09",)),
#     ]
#     return [
#         logging.makeLogRecord({**base, "levelno": level, "levelname": logging.getLevelName(level),
#                                "msg": msg, "args": args})
#         for level, msg, args in specs
#     ]
# ```
#
# Write `make_formatters()` returning a list of `(title, formatter)` pairs for these five formatters:
#
# 1. `minimal`: `%(levelname)s %(message)s`
# 2. `aligned`: level name left-aligned to width 8, then `| `, the logger name, ` | ` and the message (`%(levelname)-8s| %(name)s | %(message)s`)
# 3. `full`: `%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s` with `datefmt="%Y-%m-%d %H:%M:%S"`, in UTC
# 4. `brace style`: `{levelname}:{name}:{message}` using `style="{"`
# 5. `default time`: `%(asctime)s | %(message)s` with no `datefmt`, in UTC
#
# For each formatter print `[<title>]` and then the three records formatted with it.
