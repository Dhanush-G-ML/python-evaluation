# T08-E03: Your first decorators
#
# Write two decorators that work on functions with any signature:
#
# - `announce` prints `Calling <function name>` before the call and `Finished <function name>` afterwards, and
#   returns the original result.
# - `shout` upper-cases the (string) result of the function.
#
# Then define `add(a, b)` decorated with `@announce`, and `greet(name, punctuation="!")` decorated with `@shout`
# returning `f"hello {name}{punctuation}"`. The driver also applies `announce` manually (`sub = announce(sub)`)
# to show that `@announce` is only shorthand, and prints `add.__name__`. Notice that it is `wrapper`; the next
# exercise fixes that.
