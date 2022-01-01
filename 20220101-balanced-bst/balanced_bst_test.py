from balanced_bst import TreeNode

import pytest


@pytest.mark.parametrize(
    "list,expected",
    [
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 4),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 4),
    ],
)
def test_balanced_bst(list, expected):
    got = TreeNode.balanced_from_list(list)
    assert got.height == expected
