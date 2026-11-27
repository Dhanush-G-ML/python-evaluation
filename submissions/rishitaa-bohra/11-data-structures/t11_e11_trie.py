# T11-E11 Trie (challenge)
#
# Write a class `Trie`, also called a prefix tree, for lowercase words. Implement these methods:
#
# - `insert(word)`. Inserting a duplicate changes nothing.
# - `search(word)` is `True` only for complete words.
# - `starts_with(prefix)` is `True` when some stored word begins with the prefix.
# - `count_prefix(prefix)` returns how many stored words begin with the prefix.
# - `words_with_prefix(prefix)` returns the matching words in alphabetical order.
# - `delete(word)` returns `True` if the word was removed, and also removes branches that no other
#   word uses.
