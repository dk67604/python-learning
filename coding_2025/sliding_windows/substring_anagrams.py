def substring_anagrams(s: str, t: str) -> int:
    len_s, len_t = len(s), len(t)
    if len_t > len_s:
        return 0
    
    count = 0
    expected_freqs, window_freqs = [0] * 26, [0] * 26
    for c in t:
        expected_freqs[ord(c) - ord('a')] += 1
    left = right = 0
    while right < len_s:
        window_freqs[ord(s[right]) - ord('a')] +=1

        if right - left + 1 == len_t:
            if window_freqs == expected_freqs:
                count +=1

            window_freqs[ord(s[left]) - ord('a')] -=1
            left +=1
        right +=1
    return count