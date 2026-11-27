# T13-E08 Maze solver with BFS
#
# Load a maze from a text file. `#` is a wall, a space is open floor, `S` is the start and `E` is
# the end. Find the **shortest** path with breadth-first search, then print the maze with the path
# drawn as `*`. Validate the maze:
#
# - It needs exactly one `S` and one `E`, and no other characters.
# - Short rows are padded with walls.
#
# The program has these options:
#
# - `--visited` marks every explored cell with `.`.
# - `--compare` also runs depth-first search and prints its path, which is often longer.
#
# When there is no path, print the explored area and exit with code 2.
#
# Suggested modules: `maze.py` (`Maze`, `MazeError`, `render`), `solver.py` (`solve_bfs`,
# `solve_dfs`, `Result`), `cli.py`.
