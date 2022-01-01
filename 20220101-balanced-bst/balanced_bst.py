from typing import Any, List, Optional, Union


class TreeNode:
    def __init__(
        self,
        value: int = None,
        left: Optional[Union["TreeNode", int]] = None,
        right: Optional[Union["TreeNode", int]] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

        if left is not None and isinstance(left, int):
            self.left = TreeNode(left)
        if right is not None and isinstance(right, int):
            self.right = TreeNode(right)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, TreeNode):
            return False

        if self.value != __o.value:
            return False

        return self.left == __o.left and self.right == __o.right

    def __repr__(self) -> str:
        try:
            return f"({self.value}, {self.left}, {self.right})"
        except RecursionError:
            return "..."

    @staticmethod
    def balanced_from_list(
        list: List[int], start: Optional[int] = None, finish: Optional[int] = None
    ) -> "TreeNode":
        if start is None:
            start = 0
        if finish is None:
            finish = len(list) - 1

        if start > finish:
            return None

        mid = (finish + start) // 2
        return TreeNode(
            list[mid],
            TreeNode.balanced_from_list(list, start, mid - 1),
            TreeNode.balanced_from_list(list, mid + 1, finish),
        )

    @property
    def height(self):
        lh = self.left.height if self.left else 0
        rh = self.right.height if self.right else 0
        return 1 + max(lh, rh)
