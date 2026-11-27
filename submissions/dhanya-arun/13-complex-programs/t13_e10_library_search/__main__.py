# T13-E10 Library search with a trie (challenge)
#
# Index `data/books.csv`, which has the columns `id,title,author,year,genre`, so that searching is
# fast. The program works like this:
#
# - Split titles and authors into lowercase words, dropping stopwords such as `the`, `of` and `and`.
#   Insert each word into a **trie**, one for titles and one for authors, where each word node holds
#   the set of book ids that contain the word.
# - `search <words>` requires every query word to match the **start** of some word in the title or
#   author, so `pyth eff` finds "Effective Python". Rank the results: an exact title word scores 3,
#   an exact author word scores 2 and a prefix-only match scores 1. Ties are broken by title.
# - `title <words>` and `author <words>` limit the search to one field.
# - `suggest <prefix>` autocompletes a word, most frequent first.
# - `info <id>`, `help` and `quit` are also available.
#
# Suggested modules: `trie.py` (`Trie` with `insert`, `exact`, `prefix_ids` and `complete`),
# `catalog.py` (`Book`, `load_books`, `words`), `index.py` (`LibraryIndex` with `search` and
# `suggest`), `cli.py`.
