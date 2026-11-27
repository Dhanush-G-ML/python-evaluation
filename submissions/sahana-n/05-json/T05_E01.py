# T05-E01 - JSON basics: dumps and loads
#
# Using `json.dumps` and `json.loads` on the dictionary below:
#
# 1. Print the compact JSON text (`compact: ...`).
# 2. Print an indented version (2 spaces) with sorted keys.
# 3. Write `roundtrip(obj)` that converts an object to JSON text and back. Show how the type of `scores` changes, what `married` and `nickname` become, and whether the round trip gives an equal object.
# 4. Show what happens to integer dictionary keys: print `roundtrip({1: "a", 2: "b"})`.
# 5. Try to dump a dictionary containing a `set`, catch the `TypeError` and print its message.
