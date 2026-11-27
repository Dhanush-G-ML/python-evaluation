# T15-E06 - Fixtures with params and conftest.py
#
# Part A - the missing fixtures. Run `py -m pytest`: both tests in `test_slugify.py` show an error `fixture '...' not found`. Create `conftest.py` in the same folder. pytest reads it automatically and every test file in the folder can use its fixtures without importing them. Put these two fixtures in it:
#
# 1. `hello_variants`: a fixture with `params`, four spellings of the same title, with ids: `"Hello World"` (`plain`), `"  Hello   World  "` (`extra-spaces`), `"HELLO-world"` (`dash-and-caps`) and `"hello_world!"` (`underscore-and-bang`). It returns `request.param`. Every test that uses it runs four times.
# 2. `sentence`: a plain fixture returning `"Pytest makes testing pleasant, even for beginners"`.
#
# Part B - tests in two files. In `test_slugify.py` test that `slugify(hello_variants)` is `hello-world` for every variant, that the slug of `sentence` has no spaces and equals `pytest-makes-testing-pleasant-even-for-beginners`, and that the slug of `""` is `""`.
#
# Create a second file `test_text_stats.py` that uses the SAME `sentence` fixture from `conftest.py` and tests:
#
# - `word_count(sentence) == 7`;
# - a fixture `max_length` defined inside this file with `params=[5, 10, 20]` and ids `len5`, `len10`, `len20`; a test that `len(truncate(sentence, max_length)) <= max_length` (three runs);
# - `truncate(sentence, 10) == "Pytest ..."`, short text stays unchanged, text of exactly the limit is not shortened, and a limit shorter than the suffix raises `ValueError`;
# - `is_palindrome` is true for `"A man, a plan, a canal: Panama"` and false for `"pytest"`.
#
# Behaviours to test
#
# | Function | Behaviour |
# |----------|-----------|
# | `slugify` | lowercase, runs of other characters become one `-`, no dash at either end |
# | `truncate` | at most `length` characters; ends with `...` when shortened; short text unchanged; length below the suffix raises |
# | `word_count` | counts words split on whitespace |
# | `is_palindrome` | ignores case, spaces and punctuation |
