import pytest

from py_warmup.text import slugify


def test_slugify_empty() -> None:
    assert slugify("") == ""


def test_slugify_symbols() -> None:
    assert slugify("!*&^$&%^") == ""


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("Hello World!", "hello-world"),
        ("A unicode \u018e string \xf1", "a-unicode-string"),
    ],
)
def test_slugify_parametrize_input(input: str, expected_output: str) -> None:
    assert slugify(input) == expected_output
