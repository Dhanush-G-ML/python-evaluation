# T04-E02 - Parse sensor readings
#
# `data/readings.txt` holds temperature readings, one per line, but some lines are not numbers. Write `parse_readings(lines)` that returns `(values, bad)`: `values` is a list of floats, `bad` is a list of `(line_number, text)` for lines that cannot be converted (line numbers start at 1; text is stripped). Print: the number of lines, the number of valid readings, the list of invalid line numbers, each invalid line as `  line <n>: <text as repr>`, the average with two decimals, and the minimum and maximum.
