# T11-E01 Stack
#
# A stack is last in, first out (LIFO): the last item you push is the first one you pop. Write a
# class `Stack` that stores its items in a Python list, with these methods:
#
# - `push(item)` adds an item to the top.
# - `pop()` removes and returns the top item. It raises `IndexError` if the stack is empty.
# - `peek()` returns the top item without removing it. It raises `IndexError` if the stack is empty.
# - `is_empty()` returns `True` or `False`.
# - `len(stack)` works, because you implement `__len__`.
#
# Then write `is_balanced(text)`. It uses your `Stack` to check that every `(`, `[` and `{` in
# `text` is closed by the matching bracket in the right order. Other characters are ignored.
