# T11-E02 Queue from two stacks
#
# A queue is first in, first out (FIFO). Write a class `Queue` that uses **two Python lists** as
# stacks, an inbox and an outbox, instead of `list.pop(0)`. It needs these methods:
#
# - `enqueue(item)` adds an item at the back.
# - `dequeue()` removes and returns the front item. It raises `IndexError` if the queue is empty.
# - `front()` returns the front item without removing it.
# - `is_empty()` and `__len__`.
#
# Also write `process_jobs(jobs)`. It puts every job into a `Queue` and returns the list of jobs
# in the order they come out.
