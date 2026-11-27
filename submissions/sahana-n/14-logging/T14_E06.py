# T14-E06 - Logger hierarchy and propagation
#
# Write `build_hierarchy()` that first resets the four loggers `app`, `app.db`, `app.web` and `app.web.api` (no handlers, level `NOTSET`, `propagate = True`) and then configures:
#
# - `app`: level `INFO` and one `StreamHandler` on `sys.stdout` with the format `[%(name)s] %(levelname)s %(message)s`. This is the only handler in the hierarchy that uses this format.
# - `app.web`: level `DEBUG`.
# - `app.web.api`: its own `StreamHandler` on `sys.stdout` with the format `api> %(message)s`, and `propagate = False`.
# - `app.db`: nothing at all.
#
# Write `describe(name)` returning a dict with `name`, `level` (the logger's own level as a name), `effective` (the effective level name), `propagate` and `parent` (the parent logger's name). Write `reset_hierarchy()` that cleans the four loggers again.
#
# In the main program print the table shown below, then log these five messages and print `--- getChild ---` followed by whether `app.getChild("db") is logging.getLogger("app.db")`:
#
# 1. `app.db` DEBUG `db debug (dropped)`
# 2. `app.db` INFO `db connected`
# 3. `app.web` DEBUG `web debug (shown)`
# 4. `app.web.api` INFO `api request handled`
# 5. `app` WARNING `app warning`
