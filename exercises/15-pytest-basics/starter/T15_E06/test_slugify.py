from string_helper import slugify


def test_every_hello_variant_gives_the_same_slug(hello_variants):
    assert slugify(hello_variants) == "hello-world"


def test_slug_has_no_spaces(sentence):
    assert " " not in slugify(sentence)

# The fixtures `hello_variants` and `sentence` do not exist yet.
# Create conftest.py (exercises.md says what each fixture must contain).
