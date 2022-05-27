from collections import defaultdict
from typing import List, ValuesView


def groupAnagrams(strs: list) -> list:
    lookup = defaultdict(list)
    for word in strs:
        key = sorted(word)
        lookup[tuple(key)].append(word)
    return list(lookup.values())


if __name__ == '__main__':
    print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
