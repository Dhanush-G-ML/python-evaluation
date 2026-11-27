# T13-E07 Log analyser with regex and reports
#
# Analyse `data/access.log`, a web server log in Common Log Format:
#
# ```text
# 192.168.1.10 - - [21/Nov/2026:09:01:12 +0000] "GET /index.html HTTP/1.1" 200 5120
# ```
#
# Parse every line with **one regular expression** that has named groups. Count lines that do not
# match as malformed and report their line numbers. Print a report with these items:
#
# - The number of requests and unique IPs, the bytes sent (`-` counts as 0) and the error rate (4xx and 5xx as a percentage).
# - Counts for each status class, and the top N paths and top N IPs.
# - Requests per hour as a text bar chart, with the busiest hour marked.
# - Paths that returned 404, and suspicious IPs (3 or more 401 or 404 responses).
#
# There are also two options: `--top N` and `--status CODE`, which analyses only that status. With
# `--json FILE`, the summary is also written as JSON.
#
# Suggested modules: `parser.py` (regex, `LogEntry`, `parse_lines`), `analysis.py` (`Counter`-based
# statistics), `report.py` (text and JSON), `cli.py`.
