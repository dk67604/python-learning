def longest_substrin_with_unique_chars(s: str) -> int :
    max_len = 0
    prev_indexes = {}
    left = right = 0
    while right < len(s):
        if (s[right] in prev_indexes) and left <= prev_indexes[s[right]]:
            # Shrink ths window to exclude the previous occurrence of this character
            left = prev_indexes[s[right]] + 1
        max_len = max(max_len, right - left + 1)
        prev_indexes[s[right]] = right
        right += 1
    return max_len
