# T11-E10 Graph with an adjacency list
#
# Write a class `Graph` for an undirected graph, stored as a dict that maps each vertex to a set of
# neighbours. Implement these methods:
#
# - `add_vertex(v)` and `add_edge(a, b)`. `add_edge` creates any missing vertex.
# - `neighbours(v)` returns the neighbours as a sorted list. `degree(v)` returns how many there are.
# - `edge_count()`.
# - `has_path(start, goal)`, written with breadth-first search.
# - `components()` returns the connected groups, each one a sorted list.
