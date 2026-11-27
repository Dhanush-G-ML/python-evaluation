"""String helpers. This is the code under test: do not change it."""

import re


def slugify(text):
    """Turn text into a lowercase URL slug: 'Hello World!' becomes 'hello-world'."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")


def truncate(text, length, suffix="..."):
    """Shorten text to at most `length` characters, ending with the suffix."""
    if length < len(suffix):
        raise ValueError("length is shorter than the suffix")
    if len(text) <= length:
        return text
    return text[: length - len(suffix)] + suffix


def word_count(text):
    return len(text.split())


def is_palindrome(text):
    """Ignore case, spaces and punctuation."""
    letters = [ch.lower() for ch in text if ch.isalnum()]
    return letters == letters[::-1]
