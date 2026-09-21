from hello import greet


def test_greet_default():
    assert greet() == "Hello, Intermediate"


def test_greet_name():
    assert greet("Alex") == "Hello, Alex"


def test_greet_empty_uses_literal():
    # empty string is still a name the function echoes
    assert greet("") == "Hello, "
