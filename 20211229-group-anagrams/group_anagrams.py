from typing import FrozenSet, List, Optional, Set


def group_anagrams(input: List[str], hash_method=Optional[str]) -> Set[FrozenSet[str]]:
    groups = {}
    for word in input:
        hashed_word = _hash_word(word, hash_method)
        if hashed_word in groups:
            groups[hashed_word].append(word)
        else:
            groups[hashed_word] = [word]
    return set(frozenset(g) for g in groups.values())


def _sorting_hash(word: str) -> str:
    return "".join(sorted(word))


def _counting_hash(word: str) -> str:
    counts = [0] * 26
    for c in word:
        counts[ord(c) - ord("a")] += 1
    return "".join(str(c) for c in counts)


def _hash_word(word: str, hash_method: Optional[str]) -> str:
    methods = {
        "sorting": _sorting_hash,
        "counting": _counting_hash,
    }
    choosen_method = hash_method or "counting"
    return methods[choosen_method](word)
