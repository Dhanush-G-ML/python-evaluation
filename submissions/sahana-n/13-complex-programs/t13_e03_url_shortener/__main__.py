# T13-E03 URL shortener (in memory)
#
# Build an in-memory URL shortener with a small command prompt:
#
# - `shorten <url> [alias]` accepts only `http` and `https` URLs, and lowercases the scheme and
#   host. Without an alias it generates a code by base62-encoding a counter that starts at 1000.
#   Shortening the same URL twice returns the same code. An alias must be 3 to 20 letters, digits,
#   `-` or `_`, and must not be taken already.
# - `open <code>` prints the long URL and counts a click. A full short URL is accepted too.
# - `delete <code>` and `stats` (the most clicked links first), plus `help` and `quit`.
#
# Suggested modules: `codec.py` (`encode`, `decode` in base62), `shortener.py` (`URLShortener`,
# `Link`, `ShortenerError`), `cli.py`.
