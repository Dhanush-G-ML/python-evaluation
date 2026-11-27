# T10-E08: Decorator pattern: notifier wrappers
#
# **Pattern: Decorator (object wrapping, not the `@` syntax).** Write:
#
# - `Notifier` base class with `send(message)` (raises `NotImplementedError`).
# - `ConsoleNotifier(Notifier)`: `send` returns `CONSOLE: <message>`.
# - `NotifierDecorator(Notifier)`: stores the wrapped notifier and by default forwards `send` to it. All decorators below
#   inherit from it.
# - `PrefixDecorator(inner, prefix)`: puts `prefix` in front of the message, then forwards.
# - `TruncateDecorator(inner, max_len)`: if the message is longer than `max_len`, cut it to `max_len - 3` characters and
#   add `...`, then forward.
# - `LoggingDecorator(inner, log)`: appends `sending: <message>` (the message it received) to the list `log`, then forwards.
# - `CountingDecorator(inner)`: counts calls in `self.count`, then forwards.
#
# All of them return the result of the innermost `send`. The driver stacks four of them around a `ConsoleNotifier`; notice that the order of
# wrapping changes what each layer sees.
