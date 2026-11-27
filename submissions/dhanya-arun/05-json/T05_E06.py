# T05-E06 - Update data and write it back
#
# Write `apply_discount(products, tag, percent)` that returns a new list of product dictionaries (the input must not change). Products carrying the tag get their `price` reduced by `percent` percent, rounded to 2 decimals, and a new field `original_price` holding the old price. Other products stay as they are.
#
# Main program: load `data/products.json`, apply a 10 percent discount to the tag `sale`, save the whole shop object (all other fields preserved) to `output/products_discounted.json` with `indent=2`, load that file again and print: `Discounted: <n>`, one line per discounted product as `name` (left-aligned width 20), old price (right-aligned width 7, two decimals), ` -> `, new price (right-aligned width 6, two decimals), then `Original data untouched: True` and `Other fields kept: <shop> <currency>`.
