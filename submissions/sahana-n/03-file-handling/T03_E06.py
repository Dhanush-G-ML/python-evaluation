# T03-E06 - Folders and files with pathlib
#
# Using only `pathlib`, write:
#
# 1. `build_tree(base)` - create under `base` these files (making folders as needed), each containing one line `placeholder for <filename>`: `reports/2026/march/summary.txt`, `reports/2026/march/details.csv`, `reports/2026/april/summary.txt`, `reports/archive/readme.md`. Calling it twice must not fail.
# 2. `list_files(base)` - sorted list of all files below `base` as paths relative to `base`, written with `/` separators.
# 3. `count_by_suffix(paths)` - dictionary of file extension to count, sorted by extension.
#
# In the main program use `output/tree` as the base: print the listing, print the suffix counts, then show `name`, `stem`, `suffix` and `parent` (just the folder name) of `reports/2026/march/summary.txt`, rename that file to `summary.bak` with `with_suffix`, and print `renamed to: summary.bak | old exists: False` and the number of `.txt` files left.
