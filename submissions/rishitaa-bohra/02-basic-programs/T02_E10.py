# T02-E10 - Challenge: tic-tac-toe referee
#
# Read moves from standard input, one cell number (1 to 9) per line; `X` plays first and the players alternate. Cells are numbered left to right, top to bottom. Write `winner(board)` (returns `"X"`, `"O"` or `None`; the board is a list of 9 single characters with `" "` for empty), `render(board)` and `play(moves)` which returns `(board, result, messages)`.
#
# - Invalid moves do not change the board or the current player and add one message: `Invalid move <m>: not a number`, `Invalid move <m>: must be 1-9` or `Invalid move <m>: cell taken`.
# - Stop processing moves once someone has won or the board is full.
# - Result is `X wins`, `O wins`, `Draw` or `Game in progress`.
#
# Print the messages, then the board (empty cells show their number), then the result. Board layout is shown in the expected output.
