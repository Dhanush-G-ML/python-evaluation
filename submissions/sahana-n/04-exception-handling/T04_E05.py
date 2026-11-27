# T04-E05 - Validate input by raising
#
# Write two validators that raise exceptions instead of returning flags.
#
# `validate_age(value)`: accepts an `int`, or a string of digits (surrounding spaces allowed); returns an `int`. Raise `TypeError` for any other type (floats, `None`, `bool`, lists). Raise `ValueError` with the message `age must be a whole number, got <repr>` for non-numeric text, and `age must be between 0 and 120, got <n>` for out-of-range numbers (a string like `"-5"` is not a whole number).
#
# `validate_password(password)`: needs at least 8 characters, a digit and an upper-case letter. Raise one `ValueError` listing all missing requirements, for example `password needs at least 8 characters, a digit, an upper-case letter`.
#
# Write `attempt(check, value)` that returns `OK: <result as repr>` or `<ExceptionName>: <message>`. Print the results in the format shown.
