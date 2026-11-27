# T06-E07 - Parse a web server log with named groups
#
# `data/access.log` is in the common web-server format, for example:
#
# `10.0.0.7 - - [14/Mar/2026:09:08:18 +0000] "GET /static/app.js HTTP/1.1" 200 31518`
#
# The size is `-` when no body was sent. One line in the file is damaged. Write a compiled pattern with the named groups `ip`, `time`, `method`, `path`, `status`, `size`, and `parse_line(line)` returning a dictionary (from `groupdict()`) with `status` as `int` and `size` as `int` (0 for `-`), or `None` for lines that do not match.
#
# Print: `Parsed: <n>`, `Unparsed lines: <list of line numbers>`, `First entry: <dict>`, the number of requests per status code in code order (`  <status>: <n>`), the 3 busiest IP addresses (`  <ip>: <n>`, ties by IP), and `Total bytes: <n>`.
