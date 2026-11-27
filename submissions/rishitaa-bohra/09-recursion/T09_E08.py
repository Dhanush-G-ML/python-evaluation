# T09-E08: Tower of Hanoi
#
# Move `n` disks from peg `A` to peg `C` using peg `B`, moving one disk at a time and never placing a larger disk on a
# smaller one. Disk 1 is the smallest.
#
# - `hanoi(n, source="A", target="C", spare="B")` returns the list of moves as tuples `(disk, from_peg, to_peg)`.
# - `hanoi_move_count(n)` returns the number of moves required by formula (`2**n - 1`).
# - `is_valid_solution(n, moves)` replays a list of moves on three pegs and returns `True` only if every move is legal
#   and all disks end on peg `C` in the right order. (This helper does not need to be recursive.)
