# T12-E11 Dijkstra's shortest paths (challenge)
#
# `ROADS` is a dict of dicts that stores road distances in km:
# `graph[city][neighbour] = km`. Write these functions:
#
# - `dijkstra(graph, start)` returns `(dist, previous)`. `dist` maps every reachable city to its
#   shortest distance, and `previous` stores the city you came from. Use `heapq` as the priority
#   queue, and raise `ValueError` on a negative weight.
# - `shortest_route(graph, start, goal)` returns `(total_km, [cities...])`, or `(None, [])` if the goal cannot be reached.
