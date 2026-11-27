# T06-E05 - Validate and extract e-mail addresses
#
# Rules for a valid address: a local part of letters, digits and the characters `. _ + -`, then exactly one `@`, then a domain made of one or more labels (letters, digits, hyphen) each followed by a dot, and ending in a top-level domain of at least 2 letters. No spaces anywhere.
#
# Write `is_valid_email(text)` (the entire text must fit the rules) and `extract_emails(text)` (all valid-looking addresses inside free text). Using `data/contacts.txt` (lines of `name | email | phone`), print `Valid:` and `Invalid:` counts, each invalid address with its owner (name left-aligned width 13), the 3 most common domains (lower case, most common first, ties alphabetical) as `  <domain>: <n>`, and the result of `extract_emails` on the sentence below.
