# T11-E06 Hash map from scratch
#
# Write a class `HashMap` without using a `dict` for storage. Use a list of buckets, where each
# bucket is a list of `(key, value)` pairs (separate chaining). Implement these methods:
#
# - `put(key, value)` inserts a new pair or replaces the value of an existing key.
# - `get(key, default=None)` returns the value, or `default` if the key is missing.
# - `remove(key)` returns `True` if the key was removed and `False` otherwise.
# - `keys()`, `capacity()`, `__contains__` and `__len__`.
#
# When `size / capacity` goes above 0.75, double the number of buckets and re-insert every pair.
# Finally, write `word_count(text)`. It counts words with your `HashMap` and returns an ordinary
# dict sorted by word.
