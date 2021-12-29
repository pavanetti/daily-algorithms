from typing import List, Optional


class ListNode:
    def __init__(self, value=None, next: Optional["ListNode"] = None) -> None:
        self.value = value
        self.next = next

    @staticmethod
    def from_list(lst: List[int]) -> "ListNode":
        if len(lst) == 0:
            return None
        head = ListNode(lst[0])
        node = head
        for i in range(1, len(lst)):
            node.next = ListNode(lst[i])
            node = node.next
        return head

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ListNode):
            return False

        if self.value != __o.value:
            return False

        return self.next == __o.next

    def __repr__(self) -> str:
        try:
            return f"{self.value} -> {self.next}"
        except RecursionError:
            return "..."


def even_odd_list(node: ListNode) -> ListNode:
    current_even = evens = ListNode()
    current_odd = odds = ListNode()

    while node is not None:
        current_odd.next = node
        current_odd = current_odd.next
        node = node.next

        if node is not None:
            current_even.next = node
            current_even = current_even.next
            node = node.next

    current_odd.next = evens.next
    current_even.next = None

    return odds.next
