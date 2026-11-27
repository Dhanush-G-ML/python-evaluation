# T06-E06 - Validate and normalise phone numbers
#
# Two phone number styles are valid.
#
# - India: an optional `+91` prefix (optionally followed by a space or hyphen), then 5 digits, an optional space or hyphen, and 5 digits. Examples: `98765 43210`, `+91-98765-43213`, `+91 9876543214`.
# - US: an area code of 3 digits, either plain or in parentheses, an optional space or hyphen, 3 digits, a hyphen, and 4 digits. Examples: `(555) 123-4567`, `555-123-4568`, `(555)123-4570`.
#
# Write `phone_kind(text)` returning `"IN"`, `"US"` or `None` (whole text must match) and `normalize_phone(text)` returning `+91XXXXXXXXXX` or `+1XXXXXXXXXX` (digits only after the prefix), or `None`. Use named groups in your patterns.
#
# Using the phone column of `data/contacts.txt`: print the first 4 valid numbers as `phone` (left-aligned width 18), kind, two spaces and the normalised form; then `India: <n> | US: <n> | invalid: <n>`; then each invalid number with the owner name (left-aligned width 13).
