# T05-E04 - Analyse nested product data
#
# `data/products.json` is an object with `shop`, `currency` and a list `products`. Each product has `id`, `name`, `price`, `tags` (list), `stock` (dict of warehouse to quantity) and `dimensions`. Write:
#
# - `stock_by_warehouse(products)` - total quantity per warehouse.
# - `names_with_tag(products, tag)` - names of products that have the tag, in file order.
# - `most_expensive(products)` - the product dictionary with the highest price.
# - `out_of_stock(products)` - list of `(product name, warehouse)` pairs where the stock is 0, in file order.
#
# Print: the header `Shop: <shop> (<currency>), <n> products`; the warehouse totals sorted by name (name left-aligned width 8, quantity right-aligned width 5); `On sale:` with the names joined by `, `; `Most expensive: <name> (<price with 2 decimals>)`; `Out of stock locations: <count>`; and `First three:` followed by the first three pairs.
