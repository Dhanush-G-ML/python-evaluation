# T04-E03 - Exception tour
#
# Write `risky_calls()` returning a list of `(label, function)` pairs, one for each of these expressions (each function takes no arguments and runs the expression): `int('abc')`, `[1, 2, 3][5]`, `{'a': 1}['b']`, `10 / 0`, `open('missing_file.txt')`, `'5' + 5`, `None.upper()`. Write `describe(func)` which calls `func` and returns `"<ExceptionName>: <message>"` or `"no error"`. Print each label (left-aligned width 26), `-> ` and the description. Then print the four `issubclass` facts shown in the expected output.
