from greeting import greet


def test_greet_returns_the_requested_greeting():
    assert greet("Ada") == "Hello, Ada!"
