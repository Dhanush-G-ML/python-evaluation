# T08-E10: Class decorators and class-based decorators
#
# Decorators can receive and return classes, and a class with `__call__` can itself act as a decorator.
#
# - `REGISTRY = {}` and a class decorator `register(cls)` that stores the class under `cls.__name__` and returns it
#   unchanged.
# - A class decorator `add_repr(cls)` that gives the class a `__repr__` listing its instance attributes, such as
#   `Point(x=1, y=2)` (use `vars(self)` and `repr` of the values).
# - A class `CountCalls` used as a function decorator: it counts calls in `self.count`, forwards the call to the original
#   function, has a `reset()` method, and copies the function's `__name__` and `__doc__` with
#   `functools.update_wrapper(self, func)`.
#
# Define `Dog(name)` with `@register`, `Point(x, y)` with `@register` stacked above `@add_repr`, and
# `greet(name)` (docstring `"Say hi."`, returns `f"hi {name}"`) with `@CountCalls`.
