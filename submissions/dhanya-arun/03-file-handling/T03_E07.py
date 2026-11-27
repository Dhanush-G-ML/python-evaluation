# T03-E07 - Large file, one line at a time
#
# Never load the whole file with `read()` or `readlines()` in this exercise. Write:
#
# - `count_levels(path)` - dictionary of log level to count, for lines like `2026-03-14 09:03:10 [INFO] Server started`.
# - `first_line_with(path, level)` - the 1-based number of the first line of that level, or `None`.
# - `tail(path, n)` - the last `n` lines (without newline), using `collections.deque(f, maxlen=n)`.
# - `write_big_log(path, lines)` - writes `lines` lines `2026-03-14 00:00:00 [LEVEL] line <i>` where every 10th line is `ERROR` and the others `INFO`.
#
# Main program: for `data/server.log` print each level sorted alphabetically (level left-aligned width 8, count right-aligned width 3), the line number of the first `ERROR`, and the last 3 lines indented by two spaces. Then write `output/big.log` with 200000 lines, print the level counts of that file and its last line, and delete it.
