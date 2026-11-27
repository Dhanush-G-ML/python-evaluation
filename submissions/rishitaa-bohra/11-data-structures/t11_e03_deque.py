# T11-E03 Deque toolbox
#
# Use `collections.deque` to write three small tools:
#
# 1. `is_palindrome(text)` ignores case and every character that is not a letter or a digit. It
#    compares characters from both ends with `popleft()` and `pop()`.
# 2. `rotate_list(items, k)` returns a new list rotated `k` places to the right. A negative `k`
#    rotates to the left.
# 3. A class `RecentItems(limit)` with `add(item)` and `latest_first()`. It keeps only the last
#    `limit` items, for example a browser's recently visited pages.
