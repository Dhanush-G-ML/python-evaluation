# T08-E08: Stacking decorators
#
# When decorators are stacked, the one closest to the function is applied first.
#
# - `bold` wraps the result in `<b>...</b>`; `italic` wraps it in `<i>...</i>`.
# - `trace(label)` prints `enter <label>` before and `exit <label>` after the call.
#
# Define `hello()` returning `"hello"` decorated with `@bold` above `@italic`, and `hello_reversed()` with the
# order swapped. Define `work()` that prints `working` and returns `"done"`, decorated with `@trace("A")`,
# `@trace("B")`, `@trace("C")` from top to bottom. The driver also builds the first stack manually with function
# calls: `bold(italic(...))`.
