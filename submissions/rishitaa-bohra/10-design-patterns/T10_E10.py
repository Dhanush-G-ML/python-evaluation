# T10-E10: Iterator: lazy pages and tree traversal
#
# **Pattern: Iterator.** Write three things.
#
# 1. `PageIterator(fetch_page)`: an iterator over a paginated source. `fetch_page(n)` returns the list of items on page `n`
#    (starting at 0); an empty list means there are no more pages. The iterator must be **lazy**: a page is requested only
#    when all items of the previous page have been consumed. Implement `__iter__` (returns `self`) and `__next__`
#    (raises `StopIteration` at the end, and must not call `fetch_page` again after the end was reached).
# 2. `BinaryTree`: a binary search tree with `insert(value)` (smaller values go left, others right). Iterating it yields the
#    values in sorted order (in-order traversal) using a recursive generator and `yield from`. `reversed(tree)` yields them
#    in descending order (implement `__reversed__`). `value in tree` works through iteration.
# 3. `chunked(iterable, size)`: a generator that yields lists of at most `size` items without consuming more of the input
#    than needed (`itertools.islice` helps).
