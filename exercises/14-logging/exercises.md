# Topic 14: Logging: exercises

Work from the topic folder (the one that contains `data/`). Put your own scripts in a folder of your choice, open data files as `data/<name>` when you run from the topic folder, and write any output files into an `output/` folder (create it with `pathlib`), never into `data/`.

Use the standard library `logging` module only. Never use `print` for the log messages themselves; use it only for the report lines the exercise asks for. Pass values to the logger as arguments (`logger.info("total is %s", total)`) instead of building the string yourself with an f-string.

Expected output below was produced by running the trainer solutions with Python 3.12.

## T14-E01 - First log messages with basicConfig

**Level:** Easy  |  **Estimated time:** 10 minutes  |  **Practises:** basicConfig, the five levels, named loggers

**Data files:** none (all data is given in the exercise)

### Problem

Write `setup_logging(level)` that calls `logging.basicConfig` with the given level, the format `%(levelname)s:%(name)s:%(message)s`, `stream=sys.stdout` and `force=True` (so it can be called again with a new level).

Write `checkout(cart)` where `cart` is a list of `(name, price)` pairs. Use a logger named `shop` and return the total price:

- `DEBUG` `cart has <n> item(s)` at the start.
- An empty cart logs `ERROR` `cart is empty, nothing to charge` and returns `0.0`.
- Otherwise log `INFO` `total is <total with two decimals>`.
- A total over 100 also logs `WARNING` `large order: <total>` (two decimals).
- A total over 500 also logs `CRITICAL` `order exceeds the limit, flagged for review`.

In the main program run these three carts twice: once with level `DEBUG` (print `--- level DEBUG ---` first) and once with level `WARNING` (print `--- level WARNING ---` first):

```python
CARTS = [
    [("pen", 1.5), ("book", 12.0)],
    [],
    [("laptop", 899.0)],
]
```

### Sample input

No input.

### Expected output

```text
--- level DEBUG ---
DEBUG:shop:cart has 2 item(s)
INFO:shop:total is 13.50
DEBUG:shop:cart has 0 item(s)
ERROR:shop:cart is empty, nothing to charge
DEBUG:shop:cart has 1 item(s)
INFO:shop:total is 899.00
WARNING:shop:large order: 899.00
CRITICAL:shop:order exceeds the limit, flagged for review
--- level WARNING ---
ERROR:shop:cart is empty, nothing to charge
WARNING:shop:large order: 899.00
CRITICAL:shop:order exceeds the limit, flagged for review
```

### Hints

- `logging.getLogger("shop")` returns the same logger every time you ask for it by that name.
- The level you give `basicConfig` is the threshold of the root logger. Messages below it are dropped.
- Without `force=True`, a second `basicConfig` call does nothing because the root logger already has a handler.
- Use `%.2f` placeholders: `logger.info("total is %.2f", total)`.

### Acceptance checklist

- [ ] Each of the five levels is used at least once.
- [ ] The second run shows only `WARNING` and above.
- [ ] Messages use `%s`-style arguments, not f-strings.
- [ ] Output matches the expected output.

---

## T14-E02 - Levels and thresholds

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** level numbers, setLevel, isEnabledFor, custom level names, handlers that collect records

**Data files:** none (all data is given in the exercise)

### Problem

Register a custom level `NOTICE` with number 25 (between `INFO` and `WARNING`) using `logging.addLevelName`.

Write a handler class `ListHandler(logging.Handler)` that keeps every record it receives in a list called `records`.

Write `emitted_at(threshold)`: it uses a logger named `levels.demo` (with `propagate = False` and one `ListHandler`), sets the logger level to `threshold` (a level name such as `"WARNING"`), logs one message at each of `DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL` and returns the list of level names that were actually recorded.

Write `enabled_flags(threshold)` that returns a dict mapping each of the six level names to `logger.isEnabledFor(level)` for the same logger.

Print the level numbers, then `emitted_at` for the thresholds `DEBUG`, `NOTICE`, `WARNING` and `CRITICAL` (name left-aligned to width 9, then `-> ` and the names joined by `, `), then the `enabled_flags("ERROR")` dict.

### Sample input

No input.

### Expected output

```text
Level numbers: DEBUG=10, INFO=20, NOTICE=25, WARNING=30, ERROR=40, CRITICAL=50
DEBUG    -> DEBUG, INFO, NOTICE, WARNING, ERROR, CRITICAL
NOTICE   -> NOTICE, WARNING, ERROR, CRITICAL
WARNING  -> WARNING, ERROR, CRITICAL
CRITICAL -> CRITICAL
isEnabledFor at ERROR: {'DEBUG': False, 'INFO': False, 'NOTICE': False, 'WARNING': False, 'ERROR': True, 'CRITICAL': True}
```

### Hints

- `logging.getLevelNamesMapping()` returns a dict from level name to number (Python 3.11 and newer) and includes names you added.
- `logger.log(number, "message")` logs at any numeric level.
- A custom handler only has to implement `emit(self, record)`.
- `logger.setLevel("WARNING")` accepts a level name as a string.

### Acceptance checklist

- [ ] `NOTICE` appears between `INFO` and `WARNING` in the numbers line.
- [ ] A higher threshold lets fewer messages through.
- [ ] `ListHandler` stores records and does not print.
- [ ] Output matches the expected output.

---

## T14-E03 - Formatters

**Level:** Easy  |  **Estimated time:** 15 minutes  |  **Practises:** Formatter, format fields, datefmt, style, LogRecord

**Data files:** none (all data is given in the exercise)

### Problem

To get the same output every time, the program builds its own log records instead of logging live. The helper below is given; copy it into your program:

```python
import logging
import time

CREATED = 1_700_000_000.5  # 2023-11-14 22:13:20.5 UTC


def sample_records():
    base = {
        "name": "billing", "pathname": "/app/billing.py", "filename": "billing.py",
        "module": "billing", "funcName": "send_invoice", "lineno": 42,
        "created": CREATED, "msecs": 500.0,
    }
    specs = [
        (logging.INFO, "Invoice %s sent to %s", ("A-17", "ana@example.com")),
        (logging.WARNING, "Invoice %s is %d days late", ("A-12", 9)),
        (logging.ERROR, "Could not send invoice %s", ("A-09",)),
    ]
    return [
        logging.makeLogRecord({**base, "levelno": level, "levelname": logging.getLevelName(level),
                               "msg": msg, "args": args})
        for level, msg, args in specs
    ]
```

Write `make_formatters()` returning a list of `(title, formatter)` pairs for these five formatters:

1. `minimal`: `%(levelname)s %(message)s`
2. `aligned`: level name left-aligned to width 8, then `| `, the logger name, ` | ` and the message (`%(levelname)-8s| %(name)s | %(message)s`)
3. `full`: `%(asctime)s [%(levelname)s] %(name)s.%(funcName)s:%(lineno)d - %(message)s` with `datefmt="%Y-%m-%d %H:%M:%S"`, in UTC
4. `brace style`: `{levelname}:{name}:{message}` using `style="{"`
5. `default time`: `%(asctime)s | %(message)s` with no `datefmt`, in UTC

For each formatter print `[<title>]` and then the three records formatted with it.

### Sample input

No input.

### Expected output

```text
[minimal]
INFO Invoice A-17 sent to ana@example.com
WARNING Invoice A-12 is 9 days late
ERROR Could not send invoice A-09
[aligned]
INFO    | billing | Invoice A-17 sent to ana@example.com
WARNING | billing | Invoice A-12 is 9 days late
ERROR   | billing | Could not send invoice A-09
[full]
2023-11-14 22:13:20 [INFO] billing.send_invoice:42 - Invoice A-17 sent to ana@example.com
2023-11-14 22:13:20 [WARNING] billing.send_invoice:42 - Invoice A-12 is 9 days late
2023-11-14 22:13:20 [ERROR] billing.send_invoice:42 - Could not send invoice A-09
[brace style]
INFO:billing:Invoice A-17 sent to ana@example.com
WARNING:billing:Invoice A-12 is 9 days late
ERROR:billing:Could not send invoice A-09
[default time]
2023-11-14 22:13:20,500 | Invoice A-17 sent to ana@example.com
2023-11-14 22:13:20,500 | Invoice A-12 is 9 days late
2023-11-14 22:13:20,500 | Could not send invoice A-09
```

### Hints

- `formatter.format(record)` returns the final text of one record.
- `asctime` uses local time by default. Set `formatter.converter = time.gmtime` to use UTC.
- The default time format is `YYYY-MM-DD HH:MM:SS,mmm` (a comma before the milliseconds). Setting `datefmt` removes the milliseconds.
- `%(levelname)-8s` pads on the right, `%(levelname)8s` pads on the left.

### Acceptance checklist

- [ ] Five formatters, each used on all three records.
- [ ] The `full` formatter shows no milliseconds, the `default time` one does.
- [ ] The brace-style formatter uses `style="{"`.
- [ ] Output matches the expected output.

---

## T14-E04 - Log to a file and to the console at different levels

**Level:** Easy  |  **Estimated time:** 20 minutes  |  **Practises:** StreamHandler, FileHandler, handler levels, formatters per handler

**Data files:** none (all data is given in the exercise)

### Problem

Write `setup_logging(log_path)` that configures a logger named `tracker` (level `DEBUG`, `propagate = False`) with two handlers and returns the logger:

- A `StreamHandler` on `sys.stdout`, level `WARNING`, format `%(levelname)s: %(message)s`.
- A `FileHandler` for `log_path` (create the parent folder, mode `"w"`, UTF-8), level `DEBUG`, format `%(levelname)-8s | %(name)s | %(message)s`.

Write `close_logging(logger)` that closes and removes the handlers, and `run_tasks(logger, tasks)` for a list of `(name, milliseconds, error)` tuples. For each task log `DEBUG` `starting task <name>`. If `error` is not `None`, log `ERROR` `task <name> failed: <error>` and go to the next task. Otherwise log `INFO` `task <name> finished in <ms> ms`, and if it took more than 500 ms also `WARNING` `task <name> was slow (<ms> ms)`. Return the number of failed tasks.

```python
TASKS = [
    ("import users", 120, None),
    ("resize images", 740, None),
    ("send emails", 90, "SMTP server timed out"),
    ("build report", 300, None),
    ("sync backups", 910, None),
]
```

In the main program set up logging to `output/tracker.log`, run the tasks, close logging, print `Failed tasks: <n>`, then print `--- output/tracker.log ---` and the content of the file.

### Sample input

No input.

### Expected output

```text
WARNING: task resize images was slow (740 ms)
ERROR: task send emails failed: SMTP server timed out
WARNING: task sync backups was slow (910 ms)
Failed tasks: 1
--- output/tracker.log ---
DEBUG    | tracker | starting task import users
INFO     | tracker | task import users finished in 120 ms
DEBUG    | tracker | starting task resize images
INFO     | tracker | task resize images finished in 740 ms
WARNING  | tracker | task resize images was slow (740 ms)
DEBUG    | tracker | starting task send emails
ERROR    | tracker | task send emails failed: SMTP server timed out
DEBUG    | tracker | starting task build report
INFO     | tracker | task build report finished in 300 ms
DEBUG    | tracker | starting task sync backups
INFO     | tracker | task sync backups finished in 910 ms
WARNING  | tracker | task sync backups was slow (910 ms)
```

### Hints

- The logger level is the first filter, the handler level is the second. Set the logger to `DEBUG` so the file handler can see everything.
- Each handler has its own `setFormatter`.
- Close the file handler before you read the file back, so everything is flushed.
- `Path.mkdir(parents=True, exist_ok=True)` creates the `output` folder.

### Acceptance checklist

- [ ] The console shows only `WARNING` and above, with the short format.
- [ ] The file has every message, with the aligned format.
- [ ] The log file is written to `output/`, not to `data/`.
- [ ] Output matches the expected output.

---

## T14-E05 - Rotating log files

**Level:** Medium  |  **Estimated time:** 20 minutes  |  **Practises:** RotatingFileHandler, maxBytes, backupCount

**Data files:** none (all data is given in the exercise)

### Problem

Write `setup_logging(directory, max_bytes=200, backups=3)` that creates the folder, deletes any old `app.log*` files in it, and configures a logger named `rotating.demo` (level `INFO`, `propagate = False`) with a `RotatingFileHandler` for `app.log` (UTF-8, the given limits, format `%(message)s`). Write `close_logging(logger)` as in the last exercise.

Write `write_events(logger, count)` that logs `event <nn>: batch processed` for `nn` from 1 to `count` (two digits, `event 01`). Write `describe(directory)` that returns `(file name, line count, first line, last line)` for `app.log`, `app.log.1`, `app.log.2`, ... in that order.

In the main program write 30 events into `output/rotating` and print a table: the file name left-aligned to width 10, the line count right-aligned to width 5, two spaces, then the first 8 characters of the first line, ` -> ` and the first 8 characters of the last line. The header is shown in the expected output.

### Sample input

No input.

### Expected output

```text
file      lines  first -> last
app.log       2  event 29 -> event 30
app.log.1     7  event 22 -> event 28
app.log.2     7  event 15 -> event 21
app.log.3     7  event 08 -> event 14
```

### Hints

- When `app.log` would grow past `maxBytes`, the handler renames it to `app.log.1`, shifts the older files up and starts a new `app.log`.
- With `backupCount=3` there are never more than four files. The oldest events are deleted.
- `app.log` is always the newest file, `app.log.3` the oldest.
- Which events were lost? Work it out from the table before you read on.

### Acceptance checklist

- [ ] There are exactly four files and no `app.log.4`.
- [ ] `app.log` holds the newest events.
- [ ] You can explain why events 01 to 07 are gone.
- [ ] Output matches the expected output.

---

## T14-E06 - Logger hierarchy and propagation

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** dotted names, effective level, propagate, parent, getChild

**Data files:** none (all data is given in the exercise)

### Problem

Write `build_hierarchy()` that first resets the four loggers `app`, `app.db`, `app.web` and `app.web.api` (no handlers, level `NOTSET`, `propagate = True`) and then configures:

- `app`: level `INFO` and one `StreamHandler` on `sys.stdout` with the format `[%(name)s] %(levelname)s %(message)s`. This is the only handler in the hierarchy that uses this format.
- `app.web`: level `DEBUG`.
- `app.web.api`: its own `StreamHandler` on `sys.stdout` with the format `api> %(message)s`, and `propagate = False`.
- `app.db`: nothing at all.

Write `describe(name)` returning a dict with `name`, `level` (the logger's own level as a name), `effective` (the effective level name), `propagate` and `parent` (the parent logger's name). Write `reset_hierarchy()` that cleans the four loggers again.

In the main program print the table shown below, then log these five messages and print `--- getChild ---` followed by whether `app.getChild("db") is logging.getLogger("app.db")`:

1. `app.db` DEBUG `db debug (dropped)`
2. `app.db` INFO `db connected`
3. `app.web` DEBUG `web debug (shown)`
4. `app.web.api` INFO `api request handled`
5. `app` WARNING `app warning`

### Sample input

No input.

### Expected output

```text
logger       level    effective propagate parent
app          INFO     INFO      True      root
app.db       NOTSET   INFO      True      app
app.web      DEBUG    DEBUG     True      app
app.web.api  NOTSET   DEBUG     False     app.web
--- messages ---
[app.db] INFO db connected
[app.web] DEBUG web debug (shown)
api> api request handled
[app] WARNING app warning
--- getChild ---
app.getChild('db') is getLogger('app.db'): True
```

### Hints

- A logger with level `NOTSET` asks its parent. `getEffectiveLevel()` follows the chain up to the root.
- Records are passed to the handlers of the logger and of every ancestor (unless `propagate` is `False`). The ancestors' levels are not checked, only the level of the logger that created the record and the levels of the handlers.
- That is why the `app.web` DEBUG message appears even though `app` is at `INFO`.
- `logging.getLogger("app.db")` always returns the same object.

### Acceptance checklist

- [ ] `app.db` shows `NOTSET` as its own level and `INFO` as its effective level.
- [ ] The `api` message appears once, with only the `api>` format.
- [ ] You can explain why a DEBUG message from `app.web` is printed by a handler on `app`.
- [ ] Output matches the expected output.

---

## T14-E07 - LoggerAdapter and extra fields

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** LoggerAdapter, extra, Filter, custom format fields

**Data files:** none (all data is given in the exercise)

### Problem

Every line of a web application should show which request and user it belongs to. Use the format `%(levelname)s [req=%(request_id)s user=%(user)s] %(message)s` on a logger named `webapp` (level `DEBUG`, `propagate = False`, `StreamHandler` on `sys.stdout`).

Write:

- `ContextAdapter(logging.LoggerAdapter)`: its `process` method must merge the adapter's context with any `extra=` given on an individual call (the per-call values win).
- `DefaultsFilter(logging.Filter)` with defaults `request_id="-"` and `user="-"`. It sets an attribute only when the record does not have it, and attach it to the handler. Without it a plain `logger.info(...)` call would fail because the format needs the two fields.
- `setup_logging()` returning the logger.
- `handle_request(logger, request_id, user, path)`: create a `ContextAdapter` with `{"request_id": ..., "user": ...}`, log `INFO` `started <path>`. If the path starts with `/admin` and the user is `guest`, log `WARNING` `access denied to <path>` and return `403`. Otherwise log `DEBUG` `loading page`; if the path is `/cleanup` also log `INFO` `running as the system` with `extra={"user": "system"}`; finally log `INFO` `finished <path>` and return `200`.

Main program:

```python
logger.info("server starting")
handle_request(logger, "r-001", "ana", "/home")
handle_request(logger, "r-002", "guest", "/admin/users")
handle_request(logger, "r-003", "ana", "/cleanup")
logger.info("one-off line", extra={"user": "scheduler"})
logger.info("server stopping")
```

### Sample input

No input.

### Expected output

```text
INFO [req=- user=-] server starting
INFO [req=r-001 user=ana] started /home
DEBUG [req=r-001 user=ana] loading page
INFO [req=r-001 user=ana] finished /home
INFO [req=r-002 user=guest] started /admin/users
WARNING [req=r-002 user=guest] access denied to /admin/users
INFO [req=r-003 user=ana] started /cleanup
DEBUG [req=r-003 user=ana] loading page
INFO [req=r-003 user=system] running as the system
INFO [req=r-003 user=ana] finished /cleanup
INFO [req=- user=scheduler] one-off line
INFO [req=- user=-] server stopping
```

### Hints

- `LoggerAdapter.process(self, msg, kwargs)` returns `(msg, kwargs)`. In Python 3.12 the default version replaces any `extra` you pass on the call with the adapter's own.
- Extra keys become attributes of the record, so `%(request_id)s` can use them. Do not use names that already exist on a record (`message`, `name`, `args`, ...).
- A filter's `filter(record)` method can change the record and must return `True` to keep it.
- A missing format field does not crash your program, but the logging module prints a "Logging error" to stderr.

### Acceptance checklist

- [ ] Request lines show the request id and user from the adapter.
- [ ] The `running as the system` line shows `user=system` but still has the request id.
- [ ] Lines without context show `-` instead of failing.
- [ ] Output matches the expected output.

---

## T14-E08 - Structured logging: JSON lines

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** custom Formatter, extra fields, json.dumps, parsing logs back

**Data files:** none (all data is given in the exercise)

### Problem

Write `JsonFormatter(logging.Formatter)` whose `format(record)` returns one line of JSON with the keys `level`, `logger` and `message` (the message with its arguments filled in), followed by every extra field that was passed with `extra=`, and, when the record carries an exception, the key `exception` with the text `<ExceptionType>: <message>`. Values that JSON cannot store (such as `Decimal` and `Path`) must be turned into strings.

Write `make_logger(stream)` for a logger named `json.demo` (level `DEBUG`, `propagate = False`) with one `StreamHandler(stream)` that uses the formatter. Write `produce_lines()` that logs the following into an `io.StringIO` and returns the lines:

```python
logger.info("user %s signed in", "ana", extra={"user_id": 7, "ip": "10.0.0.5"})
logger.warning("slow payment", extra={"amount": Decimal("19.90"), "file": Path("invoices/a-17.pdf")})
try:
    {}["missing"]
except KeyError:
    logger.error("lookup failed", exc_info=True)
logger.debug("plain message")
```

Write `summarise(lines)` that parses the lines with `json.loads` and returns `(Counter of levels, list of dicts)`. The main program prints the four lines, then `Per level: <dict>`, `Lines with an exception: <list of messages>` and `Extra keys seen: <sorted list of keys other than level, logger and message>`.

### Sample input

No input.

### Expected output

```text
{"level": "INFO", "logger": "json.demo", "message": "user ana signed in", "user_id": 7, "ip": "10.0.0.5"}
{"level": "WARNING", "logger": "json.demo", "message": "slow payment", "amount": "19.90", "file": "invoices/a-17.pdf"}
{"level": "ERROR", "logger": "json.demo", "message": "lookup failed", "exception": "KeyError: 'missing'"}
{"level": "DEBUG", "logger": "json.demo", "message": "plain message"}
Per level: {'INFO': 1, 'WARNING': 1, 'ERROR': 1, 'DEBUG': 1}
Lines with an exception: ['lookup failed']
Extra keys seen: ['amount', 'exception', 'file', 'ip', 'user_id']
```

### Hints

- The standard attributes of a record are the keys of `logging.makeLogRecord({}).__dict__`. Anything else on a record came from `extra`.
- `json.dumps(payload, default=str)` handles values JSON does not know.
- `record.getMessage()` fills in the `%s` arguments. `record.exc_info` is `None` or a `(type, value, traceback)` tuple.
- Real systems add a timestamp too (for example `datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat()`). It is left out here so the output never changes.

### Acceptance checklist

- [ ] Every line is valid JSON on a single line.
- [ ] Extra fields appear as top-level keys.
- [ ] `Decimal` and `Path` values are stored as strings.
- [ ] The exception line has the `exception` key and the others do not.
- [ ] Output matches the expected output.

---

## T14-E09 - Logging exceptions with exc_info

**Level:** Medium  |  **Estimated time:** 25 minutes  |  **Practises:** logger.exception, exc_info, exception chaining, formatException

**Data files:** none (all data is given in the exercise)

### Problem

Write `ConfigError(Exception)` and `parse_amount(text)`:

- Text that is not a number raises `ConfigError("bad amount <text as repr>")` chained with `from` to the original `ValueError`.
- A negative amount raises `ValueError("negative amount")`.
- Zero raises `ValueError("zero amount")`.
- Otherwise it returns the amount as a float.

A full traceback has file paths in it, which is too noisy for this exercise. Write `BriefFormatter(logging.Formatter)` that overrides `formatException(exc_info)` and returns one line: four spaces, `raised in <function name>(): ` and then the chain of exceptions as `Type: message`, joined with ` <- `, starting with the exception itself and following `__cause__` (or `__context__`). The function name is the last frame of the traceback.

Write `setup_logging()` for a logger named `amounts` (level `DEBUG`, `propagate = False`, `StreamHandler` on `sys.stdout`, `BriefFormatter("%(levelname)s %(message)s")`) and `process(lines, logger)` that adds up the valid amounts and logs the failures in three different ways:

- `ConfigError`: `logger.exception("line <n> skipped")`
- negative amount: `logger.warning("line <n> rejected", exc_info=error)` (pass the exception object)
- zero amount: `logger.error("line <n> ignored: <error>")` without any traceback

Main program: process `["12.5", "abc", "7", "-3", "0", "2.5"]` and log `INFO` `total is <total, two decimals>`.

### Sample input

No input.

### Expected output

```text
ERROR line 2 skipped
    raised in parse_amount(): ConfigError: bad amount 'abc' <- ValueError: could not convert string to float: 'abc'
WARNING line 4 rejected
    raised in parse_amount(): ValueError: negative amount
ERROR line 5 ignored: zero amount
INFO total is 22.00
```

### Hints

- `logger.exception(...)` is `logger.error(..., exc_info=True)` and only works inside an `except` block.
- `exc_info` can be `True`, an exception instance or a `(type, value, traceback)` tuple.
- `traceback.extract_tb(tb)[-1].name` is the name of the function where the exception was raised.
- Without `exc_info` a log call never shows a traceback, even inside an `except` block.

### Acceptance checklist

- [ ] The `abc` line shows both `ConfigError` and its cause `ValueError`.
- [ ] The three failure kinds are logged at the levels and in the ways described.
- [ ] `logger.exception` is used only inside `except`.
- [ ] Output matches the expected output.

---

## T14-E10 - Analyse a log file

**Level:** Medium  |  **Estimated time:** 30 minutes  |  **Practises:** parsing log lines with regex, Counter, summaries

**Data files:** `data/app.log`

### Problem

`data/app.log` was written by the `logging` module with the format `%(asctime)s %(levelname)-8s %(name)s: %(message)s`. A line looks like this (the first lines of the file):

```text
2026-03-02 09:00:04,123 WARNING  app.auth: login failed for user bob
2026-03-02 09:00:13,123 INFO     app.web: GET /account 200 45ms
2026-03-02 09:00:23,123 DEBUG    app.db: query products took 52ms
2026-03-02 09:00:36,123 INFO     app.web: GET /cart 200 122ms
```

Write `parse_line(line)` that returns a dict with `date`, `time`, `ms`, `level`, `logger`, `message` and `minute` (`YYYY-MM-DD HH:MM`) for a log line, or `None` when the line does not match. Write `load_records(path)` that returns the parsed records of a file. Write `summarise(records)` that returns a dict with: `total`; `levels` (dict in the order DEBUG, INFO, WARNING, ERROR, CRITICAL, only levels that occur); `loggers` (list of `(name, count)`, highest count first, ties by name); `first` and `last` (`date time` text of the first and last record); `errors` (the `ERROR` and `CRITICAL` records); `busiest` (the minute with the most records, and its count; ties go to the earlier minute); and for the `app.web` messages of the form `GET <path> <status> <n>ms`: the number of requests, the average time and the slowest request line.

Print the report in the format shown in the expected output.

### Sample input

`data/app.log` (70 lines).

### Expected output

```text
Records: 70
From 2026-03-02 09:00:04 to 2026-03-02 09:10:46
By level:
  DEBUG     14
  INFO      40
  WARNING   13
  ERROR      2
  CRITICAL   1
By logger:
  app.web    40
  app.db     15
  app.auth   10
  app.jobs    5
Errors:
  09:02:35 ERROR    app.db: connection to orders-db lost
  09:06:32 ERROR    app.web: GET /checkout 500 1358ms
  09:09:49 CRITICAL app.jobs: job backup aborted: disk full
Busiest minute: 2026-03-02 09:08 (9 records)
Web requests: 40, average 238.2 ms
Slowest request: GET /checkout 500 1358ms
```

### Hints

- Use a regex with named groups. `\s+` after the level matches the padding that `%(levelname)-8s` adds.
- `Counter.most_common()` is not enough for the tie rule. Sort with `key=lambda item: (-item[1], item[0])`.
- Read the file with `encoding="utf-8"` and strip the newline from each line.
- The seconds and the millisecond part of the time are not needed for the minute.

### Acceptance checklist

- [ ] Lines that do not match the pattern are skipped, not a crash.
- [ ] Counts per level and per logger add up to the total.
- [ ] The average has one decimal and the slowest request is printed as it appears in the log.
- [ ] Output matches the expected output.

---

## T14-E11 - Challenge: log analyser for rotated files with tracebacks

**Level:** Hard  |  **Estimated time:** 40 minutes  |  **Practises:** multi-line records, rotated files, dataclasses, exception statistics, time gaps

**Data files:** `data/service.log.1`, `data/service.log`

### Problem

A service wrote its log with the `logging` module and a `RotatingFileHandler`. The older records are in `data/service.log.1` and the newer ones in `data/service.log`. Some records span several lines: a message with line breaks, or an `ERROR` written by `logger.exception`, which is followed by a traceback. The first lines of the older file:

```text
2026-03-02 10:00:10,123 INFO     shop.orders: service started with settings:
  workers=4
  retries=3
```

and one error record with its traceback:

```text
2026-03-02 10:01:15,123 ERROR    shop.payments: charge failed for order 1007
Traceback (most recent call last):
  File "/srv/shop/service.py", line 156, in make_service_logs
    action()
  File "/srv/shop/service.py", line 135, in <lambda>
    7: ("shop.payments", lambda: shop.charge(750), "charge failed for order %d"),
                                 ^^^^^^^^^^^^^^^^
  File "/srv/shop/service.py", line 108, in charge
    raise TimeoutError("payment gateway timed out")
TimeoutError: payment gateway timed out
```

Write a `Record` dataclass (`time` as `datetime`, `level`, `logger`, `message`, `extra` list of continuation lines) with a property `has_traceback` (the first continuation line is `Traceback (most recent call last):`) and a method `exception()` that returns `(exception type, text)` from the last line of the traceback, or `None`.

Write `read_records(paths)` that reads the files in the order given (oldest first) and adds every line that does not start with a timestamp to the previous record. Write `analyse(records)` returning: the count per level (in severity order), the number of multi-line records and of records with a traceback, the exceptions as `(type, count)` (highest first, ties by name) with the first record where each type was seen, the number of `ERROR` and `CRITICAL` records per minute (`HH:MM`, sorted), and the longest gap between two consecutive records (if two gaps are equal, the earlier one wins).

Print the report in the format of the expected output (one `#` per error in the minute list).

### Sample input

`data/service.log.1` (65 lines) and `data/service.log` (64 lines).

### Expected output

```text
Files read: service.log.1, service.log
Records: 70
By level: DEBUG=13, INFO=48, WARNING=3, ERROR=6
Multi-line records: 7 (with traceback: 6)
Exceptions:
  TimeoutError  3 x   first at 10:01:15 in shop.payments
  KeyError      2 x   first at 10:04:07 in shop.inventory
  ValueError    1 x   first at 10:10:22 in shop.orders
Errors per minute:
  10:01 #
  10:04 #
  10:08 #
  10:10 #
  10:12 #
  10:14 #
Longest quiet gap: 180s between 10:04:50 and 10:07:50
```

### Hints

- A timestamp line matches `^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} `. Anything else is a continuation line.
- `datetime.strptime(text, "%Y-%m-%d %H:%M:%S,%f")` reads the milliseconds with `%f`.
- Read the files in the right order. If you swap them, the first record is newer than the last one.
- The last line of a traceback looks like `KeyError: 'gizmo'`. Match `^(\w+Error|\w+Exception): ?(.*)$` for the type and the text.
- `zip(records, records[1:])` gives consecutive pairs.

### Acceptance checklist

- [ ] The two files are treated as one continuous log, oldest first.
- [ ] Traceback lines are never counted as records.
- [ ] Exception types come from the last traceback line, and the count per type is correct.
- [ ] The longest gap is taken between consecutive records of the combined log.
- [ ] Output matches the expected output.

---

## T14-E12 - Challenge: a small shop app with per-module loggers and dictConfig

**Level:** Hard  |  **Estimated time:** 60 minutes  |  **Practises:** getLogger(__name__), dictConfig, handlers/formatters/filters in a dict, custom factories, rotating and JSON logs

**Data files:** `data/shop_orders.json`

### Problem

Build a package named `shop` (a folder `shop/` with `__init__.py`) with these modules. Each module that logs creates its logger with `logger = logging.getLogger(__name__)`, so the logger names are `shop.inventory`, `shop.payments` and `shop.orders`.

- `shop/inventory.py`: a `STOCK` dict, `load_stock()` (widget 10, gadget 3, gizmo 3, doohickey 0; logs `DEBUG` `stock loaded: <dict>`), `reserve(sku, qty)` and `release(sku, qty)`. `reserve` logs `DEBUG` `checking stock for <sku> x<qty>`, raises `UnknownProduct(sku)` for an unknown product and `OutOfStock("<sku>: wanted <qty>, have <n>")` when there is not enough, otherwise lowers the stock and logs `INFO` `reserved <qty> x <sku>`; when one or no items are left it also logs `WARNING` `low stock for <sku>: <n> left`. `release` adds the stock back and logs `DEBUG` `released <qty> x <sku>`.
- `shop/payments.py`: `charge(card, amount)` logs `DEBUG` `contacting the gateway for card <card>`, `INFO` `charging <amount, two decimals> to card <card>`, raises `PaymentDeclined("amount <amount> is over the limit of <limit>")` (two decimals, limit 1000) or logs `INFO` `payment accepted`.
- `shop/orders.py`: `place_order(order)` logs `INFO` `order <id> received from <customer>`, reserves every item, charges the card, and on `OutOfStock`, `UnknownProduct` or `PaymentDeclined` releases what was reserved, logs `ERROR` `order <id> failed: <exception>` with `exc_info=True` and returns `False`. On success it logs `INFO` `order <id> completed` and returns `True`.
- `shop/formatting.py`: a `MaskFilter` (replaces card numbers of 12 to 16 digits with `*` characters and the last four digits), a `CompactFormatter` (takes `fmt` and `show_exception`; an exception is shown as `    raised in <function>(): <Type>: <message>`, or not at all when `show_exception` is false) and a `JsonFormatter` (as in T14-E08).
- `shop/config.py`: `build_config(log_dir)` returns a **configuration dictionary** for `logging.config.dictConfig`, and `setup_logging(log_dir)` creates the folder and applies it.
- `shop/app.py`: `run_orders(path)` loads the stock, reads the JSON orders, places each one, and also makes two calls on a logger named `thirdparty`: `info("this INFO line is hidden by the root level")` and `warning("a library warns on the root logger")`. It returns a dict from order id to the result.

The configuration (use `"version": 1` and `"disable_existing_loggers": False`) must contain:

- Formatter `brief`: `CompactFormatter`, `%(levelname)-7s %(name)s: %(message)s`, `show_exception` false.
- Formatter `detailed`: `CompactFormatter`, `%(levelname)-7s %(name)s.%(funcName)s: %(message)s`.
- Formatter `json`: `JsonFormatter`.
- Filter `mask`: `MaskFilter`.
- Handler `console`: `StreamHandler` on `ext://sys.stdout`, level `INFO`, formatter `brief`, filter `mask`.
- Handler `file`: `FileHandler` for `shop.log` (mode `w`), level `DEBUG`, formatter `detailed`, filter `mask`.
- Handler `errors`: `RotatingFileHandler` for `errors.jsonl` (mode `w`, 10000 bytes, 2 backups), level `ERROR`, formatter `json`, filter `mask`.
- Logger `shop`: level `DEBUG`, handlers `console`, `file` and `errors`, `propagate` false.
- Logger `shop.payments`: level `INFO`, no handlers of its own.
- Root logger: level `WARNING`, handler `console`.

The main program writes the logs into `output/shop`, runs the orders in `data/shop_orders.json`, and prints: `--- console ---` and then everything the console handler shows; `--- logger table ---` with name, own level, effective level, `propagate` and the handler class names of the four loggers `shop`, `shop.inventory`, `shop.payments`, `shop.orders`; then (after logging is shut down) the content of `shop.log`, the content of `errors.jsonl` and `Completed <n> of <m> orders: <ids>`.

### Sample input

`data/shop_orders.json` (six orders; one asks for too many gizmos, one is over the card limit, one has an unknown product). The first order:

```json
{
  "id": "A-100",
  "customer": "ana",
  "items": [
    {
      "sku": "widget",
      "qty": 2
    }
  ],
  "card": "4111111111111111",
  "amount": 25.0
}
```

### Expected output

```text
--- console ---
INFO    shop.orders: order A-100 received from ana
INFO    shop.inventory: reserved 2 x widget
INFO    shop.payments: charging 25.00 to card ************1111
INFO    shop.payments: payment accepted
INFO    shop.orders: order A-100 completed
INFO    shop.orders: order A-101 received from bob
INFO    shop.inventory: reserved 2 x gadget
WARNING shop.inventory: low stock for gadget: 1 left
INFO    shop.payments: charging 60.00 to card ************5559
INFO    shop.payments: payment accepted
INFO    shop.orders: order A-101 completed
INFO    shop.orders: order A-102 received from carla
ERROR   shop.orders: order A-102 failed: gizmo: wanted 5, have 3
INFO    shop.orders: order A-103 received from dev
INFO    shop.inventory: reserved 1 x widget
INFO    shop.payments: charging 2500.00 to card ***********0005
ERROR   shop.orders: order A-103 failed: amount 2500.00 is over the limit of 1000.00
INFO    shop.orders: order A-104 received from erin
ERROR   shop.orders: order A-104 failed: sprocket
INFO    shop.orders: order A-105 received from finn
INFO    shop.inventory: reserved 3 x widget
INFO    shop.inventory: reserved 1 x gadget
WARNING shop.inventory: low stock for gadget: 0 left
INFO    shop.payments: charging 42.00 to card ************0000
INFO    shop.payments: payment accepted
INFO    shop.orders: order A-105 completed
WARNING thirdparty: a library warns on the root logger
--- logger table ---
logger         level    effective  propagate handlers
shop           DEBUG    DEBUG      False     StreamHandler,FileHandler,RotatingFileHandler
shop.inventory NOTSET   DEBUG      True      -
shop.payments  INFO     INFO       True      -
shop.orders    NOTSET   DEBUG      True      -
--- output/shop/shop.log ---
DEBUG   shop.inventory.load_stock: stock loaded: {'widget': 10, 'gadget': 3, 'gizmo': 3, 'doohickey': 0}
INFO    shop.orders.place_order: order A-100 received from ana
DEBUG   shop.inventory.reserve: checking stock for widget x2
INFO    shop.inventory.reserve: reserved 2 x widget
INFO    shop.payments.charge: charging 25.00 to card ************1111
INFO    shop.payments.charge: payment accepted
INFO    shop.orders.place_order: order A-100 completed
INFO    shop.orders.place_order: order A-101 received from bob
DEBUG   shop.inventory.reserve: checking stock for gadget x2
INFO    shop.inventory.reserve: reserved 2 x gadget
WARNING shop.inventory.reserve: low stock for gadget: 1 left
INFO    shop.payments.charge: charging 60.00 to card ************5559
INFO    shop.payments.charge: payment accepted
INFO    shop.orders.place_order: order A-101 completed
INFO    shop.orders.place_order: order A-102 received from carla
DEBUG   shop.inventory.reserve: checking stock for gizmo x5
ERROR   shop.orders.place_order: order A-102 failed: gizmo: wanted 5, have 3
    raised in reserve(): OutOfStock: gizmo: wanted 5, have 3
INFO    shop.orders.place_order: order A-103 received from dev
DEBUG   shop.inventory.reserve: checking stock for widget x1
INFO    shop.inventory.reserve: reserved 1 x widget
INFO    shop.payments.charge: charging 2500.00 to card ***********0005
DEBUG   shop.inventory.release: released 1 x widget
ERROR   shop.orders.place_order: order A-103 failed: amount 2500.00 is over the limit of 1000.00
    raised in charge(): PaymentDeclined: amount 2500.00 is over the limit of 1000.00
INFO    shop.orders.place_order: order A-104 received from erin
DEBUG   shop.inventory.reserve: checking stock for sprocket x1
ERROR   shop.orders.place_order: order A-104 failed: sprocket
    raised in reserve(): UnknownProduct: sprocket
INFO    shop.orders.place_order: order A-105 received from finn
DEBUG   shop.inventory.reserve: checking stock for widget x3
INFO    shop.inventory.reserve: reserved 3 x widget
DEBUG   shop.inventory.reserve: checking stock for gadget x1
INFO    shop.inventory.reserve: reserved 1 x gadget
WARNING shop.inventory.reserve: low stock for gadget: 0 left
INFO    shop.payments.charge: charging 42.00 to card ************0000
INFO    shop.payments.charge: payment accepted
INFO    shop.orders.place_order: order A-105 completed
--- output/shop/errors.jsonl ---
{"level": "ERROR", "logger": "shop.orders", "message": "order A-102 failed: gizmo: wanted 5, have 3", "exception": "OutOfStock: gizmo: wanted 5, have 3"}
{"level": "ERROR", "logger": "shop.orders", "message": "order A-103 failed: amount 2500.00 is over the limit of 1000.00", "exception": "PaymentDeclined: amount 2500.00 is over the limit of 1000.00"}
{"level": "ERROR", "logger": "shop.orders", "message": "order A-104 failed: sprocket", "exception": "UnknownProduct: sprocket"}
Completed 3 of 6 orders: A-100, A-101, A-105
```

### Hints

- A formatter, filter or handler entry with a `"()"` key is created by calling that factory with the other keys as arguments. The factory can be a dotted path string such as `"shop.formatting.MaskFilter"`.
- `ext://sys.stdout` in a dictConfig dictionary is replaced by the real `sys.stdout` object.
- Handlers have the filters. Logger filters do not run for records that come from child loggers, which is why `mask` is attached to the handlers.
- `shop.payments` has its own level (`INFO`) but no handlers. Its records still reach the handlers of `shop` through propagation, so its `DEBUG` messages vanish from every output while `shop.inventory` DEBUG messages reach `shop.log`.
- `thirdparty` is not configured. It propagates to the root logger, whose level is `WARNING` and whose handler is `console`.
- Call `logging.shutdown()` (and remove the handlers) before you read the files back.

### Acceptance checklist

- [ ] The whole configuration is one dictionary applied with `dictConfig`, and no handler is created by hand.
- [ ] Every module uses `getLogger(__name__)`.
- [ ] Card numbers are masked on the console and in both files.
- [ ] The DEBUG lines of `shop.inventory` are only in `shop.log`, the payment DEBUG line is nowhere.
- [ ] `errors.jsonl` has only the three failed orders, one JSON object per line.
- [ ] The `thirdparty` warning shows on the console and its INFO line does not.
- [ ] Output matches the expected output.
