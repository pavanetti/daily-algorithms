from zeroing_lines import zero_lines


def test_zero_lines():
    matrix = [[1, 2, 3, 4], [5, 0, 7, 8], [6, 1, 1, 2], [2, 3, 4, 0]]
    expected = [[1, 0, 3, 0], [0, 0, 0, 0], [6, 0, 1, 0], [0, 0, 0, 0]]

    zero_lines(matrix)

    assert matrix == expected
