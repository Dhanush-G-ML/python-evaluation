# T09-E11: Sudoku-lite (4x4 solver)
#
# A 4x4 sudoku uses the digits 1 to 4; each row, column and 2x2 box must contain every digit exactly once. Empty cells
# are `0`. Use the `PUZZLE` below.
#
# - `can_place(grid, row, col, value)`: `True` if `value` does not already appear in that row, column or 2x2 box.
# - `solve(grid)`: returns a **solved copy** of the grid, or `None` if there is no solution. The input grid must not be
#   modified.
# - `count_solutions(grid, limit=2)`: number of solutions, stopping early once `limit` is reached (never return more than
#   `limit`). A well-formed puzzle has exactly one.
