from even_odd_list import ListNode, even_odd_list


def test_even_odd_list_equality():
    a = ListNode(1, ListNode(2))
    b = ListNode(1, ListNode(2))
    c = ListNode(1)

    assert a == b
    assert a != c


def test_list_node_from_list():
    got = ListNode.from_list([1, 2, 3])
    expected = ListNode(1, ListNode(2, ListNode(3)))

    assert got == expected


def test_even_odd_list_case1():
    input = ListNode.from_list([1, 3, 5, 7])
    output = ListNode.from_list([1, 5, 3, 7])

    assert even_odd_list(input) == output


def test_even_odd_list_case2():
    input = ListNode.from_list([1, 2, 3, 4, 5])
    output = ListNode.from_list([1, 3, 5, 2, 4])

    assert even_odd_list(input) == output
