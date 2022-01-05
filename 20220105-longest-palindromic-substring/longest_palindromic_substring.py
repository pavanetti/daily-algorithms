from math import ceil


def brute_force_lps(text: str) -> str:
    size = len(text)
    lps = ""
    for i in range(size):
        for j in range(i, size):
            if (j + 1 - i) > len(lps) and is_palindromic(text[i:j + 1]):
                lps = text[i:j + 1]
    return lps


def optimized_lps(text: str) -> str:
    size = len(text)

    def longestFrom(a, b):
        while a >= 0 and b < size and text[a] == text[b]:
            a -= 1
            b += 1
        return text[a + 1: b]

    longest = ""
    for i in range(size):
        odd = longestFrom(i, i)
        even = longestFrom(i, i + 1)
        longest = odd if len(odd) > len(longest) else longest
        longest = even if len(even) > len(longest) else longest
    return longest


def longest_palindromic_substring(
    text: str,
    algorithm=brute_force_lps,
) -> str:
    return algorithm(text)


def is_palindromic(text: str) -> bool:
    n = len(text)
    for i in range(ceil(n / 2)):
        if text[i] != text[-(i + 1)]:
            return False
    return True
