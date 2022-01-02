def reverse_words_order(words: str) -> str:
    words = list(words)
    i, j = 0, len(words) - 1
    reverse_slice(words, i, j)

    next_word = 0
    while next_word < len(words):
        i, j = next_word, next_word
        while j + 1 < len(words) and words[j + 1] != " ":
            j += 1
        next_word = j + 2
        reverse_slice(words, i, j)
    return "".join(words)


def reverse_slice(slice, i, j):
    while i < j:
        slice[i], slice[j] = slice[j], slice[i]
        i += 1
        j -= 1
