# T07-E04: Vector2D with dunder methods
#
# Write a class `Vector2D(x, y)` that behaves like a number-ish value:
#
# - `repr(v)` gives `Vector2D(3, 4)`; `str(v)` gives `(3, 4)`.
# - `v1 + v2` and `v1 - v2` return new vectors. Adding anything that is not a `Vector2D` must raise
#   the normal `TypeError` (return `NotImplemented` rather than raising yourself).
# - `v * number` and `number * v` scale the vector.
# - `v1 == v2` compares coordinates.
# - `abs(v)` returns the length (`math.hypot`).
# - `bool(v)` is `False` only for the zero vector.
# - Iterating over a vector yields `x` then `y`, so `x, y = v` works.
