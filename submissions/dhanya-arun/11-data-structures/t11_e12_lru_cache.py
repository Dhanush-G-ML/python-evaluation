# T11-E12 LRU cache (challenge)
#
# Write a class `LRUCache(capacity)` that keeps at most `capacity` entries. When it is full, it
# evicts the least recently used entry. You must not use `OrderedDict` or `functools.lru_cache`.
# Combine a dict, which maps each key to a node, with your own doubly linked list, which keeps the
# usage order. Implement these methods:
#
# - `get(key, default=None)` marks the entry as most recently used and counts a hit or a miss.
# - `put(key, value)` inserts or updates an entry. It returns the evicted key, or `None`.
# - `keys()` returns the keys from most to least recently used.
# - `__len__`, plus the attributes `hits` and `misses`.
#
# A capacity below 1 raises `ValueError`.
