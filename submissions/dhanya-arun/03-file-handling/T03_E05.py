# T03-E05 - Filter and write a CSV
#
# Write `filter_big_orders(src, dst, min_units=10)` that reads `data/sales.csv` and writes a new CSV to `dst` containing only the rows with `units >= min_units`, with an extra last column `total` (units times unit price, two decimals). Keep the original column order, then `total`. Return the number of rows written. In the main program write `output/big_orders.csv`, print `Rows kept: <n>`, then print the first 6 lines of the new file (the header and 5 rows) with the fields joined by `, `.
