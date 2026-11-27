# T10-E04: Builder: logging setup
#
# **Pattern: Builder.** Write `LoggerBuilder`, which produces a real `logging.Logger`:
#
# - `name(name)`: logger name (required).
# - `level(level_name)`: case-insensitive level name such as `"info"` or `"DEBUG"`; default is INFO. An unknown name
#   raises `ValueError(f"Unknown level: {level_name}")` immediately.
# - `stream(stream, fmt="%(levelname)s: %(message)s")`: add a handler that writes to a file-like object using the
#   given format. It can be called several times.
# - `build()`: raises `ValueError("logger needs a name")` or `ValueError("logger needs at least one handler")` when
#   incomplete; otherwise configures and returns the logger. It must remove any existing handlers (the `logging` module caches
#   loggers by name, so building twice would otherwise duplicate output) and set `propagate = False`.
#
# Every step method returns `self` so the calls can be chained.
