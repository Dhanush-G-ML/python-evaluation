# T04-E04 - try, except, else, finally
#
# Write `read_first_line(path)` that returns `(first_line, steps)`. `steps` is a list of strings recording the blocks that ran, in order: `try: opening file`, then either `except: file not found` (when the file is missing, and the result is `None`) or `else: read succeeded`, and always `finally: always runs` at the end. Also write `finally_before_return()` whose `try` block does `return "value from try", log` and whose `finally` block appends `finally ran before return` to `log`.
#
# Main program: run `read_first_line` on `data/readings.txt` and on `data/nope.txt` and print the result and each step (indented two spaces), then print the value and log from `finally_before_return()` as `value | log`.
