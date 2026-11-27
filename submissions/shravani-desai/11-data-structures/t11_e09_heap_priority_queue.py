# T11-E09 Heaps and priority queues with heapq
#
# Use the `heapq` module to write these tools:
#
# 1. `k_smallest(numbers, k)` uses `heapify` and `heappop`.
# 2. `k_largest(numbers, k)` keeps a min-heap of size `k` while it scans the numbers. It returns
#    the result in descending order.
# 3. Use `heapq.merge` to merge several sorted lists.
# 4. A class `TaskQueue` with `add(task, priority)`, `pop()` and `__len__`. `pop()` returns a
#    `(task, priority)` pair. The lowest priority number comes out first, and tasks with the same
#    priority come out in the order they were added.
