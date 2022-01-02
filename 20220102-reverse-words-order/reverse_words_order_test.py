import pytest

from reverse_words_order import reverse_words_order


@pytest.mark.parametrize(
    "input,expected",
    [
        ("Banana", "Banana"),
        ("Alice likes Bob", "Bob likes Alice"),
    ],
)
def test_reverse_words_order(input, expected):
    assert reverse_words_order(input) == expected
