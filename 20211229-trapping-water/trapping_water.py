from typing import List


def trap_water_v1(hs: List[int]) -> int:
    total = 0

    for i in range(1, len(hs) - 1):
        level = min(max(hs[: i + 1]), max(hs[i:]))
        water = level - hs[i]
        total += water
    return total


def trap_water_v2(hs: List[int]) -> int:
    total = 0
    len_hs = len(hs)

    lmax = [0] * len_hs
    rmax = [0] * len_hs
    for i in range(1, len_hs):
        j = -i  # len_hs - i - 1
        lmax[i] = max(lmax[i - 1], hs[i])
        rmax[j] = max(rmax[j + 1], hs[j])

    for i in range(1, len_hs - 1):
        level = min(lmax[i], rmax[i])
        water = level - hs[i]
        total += water
    return total


def trap_water_v3(hs: List[int]) -> int:
    total = 0

    i, j = 0, len(hs) - 1
    lmax, rmax = hs[i], hs[j]
    while i <= j:
        lmax, rmax = max(lmax, hs[i]), max(rmax, hs[j])
        if lmax < rmax:
            total += lmax - hs[i]
            i += 1
        else:
            total += rmax - hs[j]
            j -= 1
    return total


trap_water = trap_water_v3
