# T07-E01: Book with progress tracking
#
# Write a class `Book` that is created with `title`, `author` and `pages`. It must also have an attribute
# `current_page` that starts at `0`.
#
# - `describe()` returns a string like `'Dune' by Frank Herbert (412 pages)` (title in single quotes).
# - `read(count)` moves `current_page` forward by `count` pages but never past the last page.
# - `progress()` returns the percentage read, rounded to one decimal place (`current_page / pages * 100`).
