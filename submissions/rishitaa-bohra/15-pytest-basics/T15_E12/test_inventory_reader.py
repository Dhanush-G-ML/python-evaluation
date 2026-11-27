# T15-E12 - Challenge: test a JSON-reading function with fixtures and parametrize
#
# `load_products(path)` reads a JSON inventory file and returns a list of clean records. Read the code to see the rules, then write the tests. Do not read `sample_inventory.json` from the tests: create small files in `tmp_path` so that each test controls its own data.
#
# Fixtures in `conftest.py`:
#
# 1. `write_json`: uses `tmp_path` and returns a function `_write(data, name="inventory.json")` that dumps a Python object as JSON into `tmp_path` and returns the path (a factory fixture).
# 2. `write_text`: the same for raw text (needed for broken JSON).
# 3. `valid_file`: uses `write_json` to write four products: Pen (1.5, qty 100), Notebook (price as the string `"3.25"`, qty 40), Stapler (8, qty 5) and Ruler (0.9, no qty).
#
# Tests (group them in classes `TestLoadProducts`, `TestBadInput`, `TestTotals`):
#
# - Valid file: the first record is `{"name": "Pen", "price": 1.5, "qty": 100}` and there are four; the string price becomes the float `3.25`; a missing `qty` becomes 0; names are stripped of spaces; an empty list `[]` gives `[]`; a missing file raises `FileNotFoundError`.
# - Broken JSON (`'{"name": "Pen", '`) raises `ValueError` matching `invalid JSON`.
# - Parametrize with `pytest.param(..., id=...)`: the top-level document must be a list. Try an object, a string, a number and `null`; each raises `ValueError` matching `top level must be a list`.
# - Parametrize the bad records (use `pytest.param(records, message, id=...)`, ten cases) and check the exact position-based message with `match=`:
#
# | id | record(s) | message contains |
# |----|-----------|------------------|
# | no-name | `{"price": 1}` | `record 1: missing key 'name'` |
# | no-price | `{"name": "Pen"}` | `record 1: missing key 'price'` |
# | blank-name | second record has name `" "` | `record 2: name is empty` |
# | text-price | price `"free"` | `record 1: price is not a number` |
# | null-price | price `null` | `record 1: price is not a number` |
# | negative-price | price `-1` | `record 1: price cannot be negative` |
# | fractional-qty | qty `2.5` | `record 1: qty must be a whole number` |
# | negative-qty | qty `-3` | `record 1: qty must be a whole number` |
# | boolean-qty | qty `true` | `record 1: qty must be a whole number` |
# | record-not-object | the record is the string `"Pen"` | `record 1: must be an object` |
#
# - Totals: `total_value(load_products(valid_file))` is 320 (150 + 130 + 40); `total_value([])` is 0; `load_summary(valid_file)` is `{"count": 4, "units": 145, "value": 320.0}`; `load_summary` of a bad document raises `ValueError`.
#
# Run with `py -m pytest --cov=inventory_reader --cov-report=term-missing --cov-fail-under=90`.
#
# Behaviours to test
#
# See the lists and the table above. The code has nine different error messages; a good suite triggers each of them.
