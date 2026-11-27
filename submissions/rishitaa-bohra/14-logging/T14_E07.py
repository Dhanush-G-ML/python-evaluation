# T14-E07 - LoggerAdapter and extra fields
#
# Every line of a web application should show which request and user it belongs to. Use the format `%(levelname)s [req=%(request_id)s user=%(user)s] %(message)s` on a logger named `webapp` (level `DEBUG`, `propagate = False`, `StreamHandler` on `sys.stdout`).
#
# Write:
#
# - `ContextAdapter(logging.LoggerAdapter)`: its `process` method must merge the adapter's context with any `extra=` given on an individual call (the per-call values win).
# - `DefaultsFilter(logging.Filter)` with defaults `request_id="-"` and `user="-"`. It sets an attribute only when the record does not have it, and attach it to the handler. Without it a plain `logger.info(...)` call would fail because the format needs the two fields.
# - `setup_logging()` returning the logger.
# - `handle_request(logger, request_id, user, path)`: create a `ContextAdapter` with `{"request_id": ..., "user": ...}`, log `INFO` `started <path>`. If the path starts with `/admin` and the user is `guest`, log `WARNING` `access denied to <path>` and return `403`. Otherwise log `DEBUG` `loading page`; if the path is `/cleanup` also log `INFO` `running as the system` with `extra={"user": "system"}`; finally log `INFO` `finished <path>` and return `200`.
#
# Main program:
#
# ```python
# logger.info("server starting")
# handle_request(logger, "r-001", "ana", "/home")
# handle_request(logger, "r-002", "guest", "/admin/users")
# handle_request(logger, "r-003", "ana", "/cleanup")
# logger.info("one-off line", extra={"user": "scheduler"})
# logger.info("server stopping")
# ```
