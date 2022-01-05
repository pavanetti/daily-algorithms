import pytest

from longest_palindromic_substring import (longest_palindromic_substring,
                                           optimized_lps)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("programming", "mm"),
        ("bananas", "anana"),
        ("xabax", "xabax"),
        ("mind", "m"),
    ],
)
def test_longest_palindromic_substring(input: str, expected: str):
    assert expected == longest_palindromic_substring(
        input,
        algorithm=optimized_lps,
    )
