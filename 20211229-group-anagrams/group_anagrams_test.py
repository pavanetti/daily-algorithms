import pytest
from group_anagrams import group_anagrams


@pytest.mark.parametrize("hash_method", [None, "sorting", "counting"])
def test_group_anagrams(hash_method):
    input = ["yx", "abe", "act", "eab", "x", "eba", "tca", "xy"]
    expected = {
        frozenset(["abe", "eab", "eba"]),
        frozenset(["act", "tca"]),
        frozenset(["xy", "yx"]),
        frozenset(["x"]),
    }
    assert group_anagrams(input, hash_method) == expected
