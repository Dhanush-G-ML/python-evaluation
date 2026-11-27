# T10-E02: Factory: notification senders
#
# **Pattern: Factory.** Build a small notification service.
#
# - An abstract base class `Notifier` with an abstract method `send(recipient, message)` returning a string.
# - A dictionary `NOTIFIERS = {}` and a decorator factory `register(kind)` that stores a class in it.
# - Three concrete notifiers, registered as `"email"`, `"sms"` and `"push"`:
#   - `EmailNotifier.send` returns `EMAIL to <recipient>@example.com: <message>`
#   - `SmsNotifier.send` returns `SMS to <recipient>: <first 20 characters of the message>`
#   - `PushNotifier.send` returns `PUSH to <recipient>: <message in upper case>`
# - `create_notifier(kind)` returns a new notifier instance. An unknown kind raises
#   `ValueError(f"Unknown notifier: {kind} (choose from ...)")`, where the choices are the sorted registered names
#   separated by `, `.
#
# Adding a fourth notifier must need no change to `create_notifier`.
