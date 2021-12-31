from typing import List


def zero_lines(matrix: List[List[int]]) -> None:
    _foreach_element(matrix, _set_lines_as_none_if_zero)
    _foreach_element(matrix, _replace_none_with_zero)


def _set_lines_as_none_if_zero(matrix: List[List[int]], r: int, c: int) -> None:
    if matrix[r][c] == 0:
        _foreach_from_row(matrix, r, _set_line_as_none)
        _foreach_from_column(matrix, c, _set_line_as_none)


def _set_line_as_none(matrix: List[List[int]], r: int, c: int) -> None:
    if matrix[r][c] != 0:
        matrix[r][c] = None


def _replace_none_with_zero(matrix: List[List[int]], r: int, c: int) -> None:
    if matrix[r][c] is None:
        matrix[r][c] = 0


# helper iterators


def _foreach_element(matrix: List[List[int]], func: callable) -> None:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            func(matrix, i, j)


def _foreach_from_column(matrix: List[List[int]], c: int, func: callable) -> None:
    for i in range(len(matrix)):
        func(matrix, i, c)


def _foreach_from_row(matrix: List[List[int]], r: int, func: callable) -> None:
    for j in range(len(matrix[r])):
        func(matrix, r, j)
