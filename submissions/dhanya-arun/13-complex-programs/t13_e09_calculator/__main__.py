# T13-E09 Tokenizer plus calculator (challenge)
#
# Build an interactive calculator in three stages:
#
# 1. **Tokenizer.** Turn text into `Token(kind, text, pos)` items of kind NUMBER (including `3.5`,
#    `.5` and `1e3`), NAME, OP (`+ - * / // % ** ^ =`, where `^` means `**`), LPAREN, RPAREN and
#    COMMA, followed by an END token. Report an unknown character together with its position.
# 2. **Parser.** A recursive-descent parser that builds a tree of small dataclasses. The usual
#    precedence rules apply, unary minus binds more loosely than `**` (so `-2 ** 2` is `-4`), and
#    `**` is right-associative (so `2 ^ 3 ^ 2` is 512). It supports assignment (`x = 3`), calls
#    (`max(1, 2, 3)`) and brackets.
# 3. **Evaluator.** Supports variables, `ans` (the last result), the constants `pi` and `e`, and the
#    functions `sqrt`, `abs`, `round`, `log`, `min` and `max`, with argument-count checks.
#
# Errors such as syntax errors, unknown names, division by zero and wrong argument counts print a
# `^` under the position of the problem. The commands `:tokens <expr>`, `:vars`, `:help` and
# `:quit` are also available.
#
# Suggested modules: `errors.py` (`CalcError` with `pos`), `tokenizer.py`, `parser.py`
# (grammar in its docstring), `evaluator.py`, `cli.py`.
