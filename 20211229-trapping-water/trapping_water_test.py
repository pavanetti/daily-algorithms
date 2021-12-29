from trap_water import trap_water


def test_trap_water():
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert trap_water(heights) == 6
