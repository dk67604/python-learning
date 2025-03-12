def substring_anagrams(s: str, t: str) -> int:
    """
    Given two strings `s` and `t`, count the number of substrings in `s` 
    that are anagrams of `t`.

    Approach:
    - Use a **Sliding Window** of size `len(t)`.
    - Maintain **frequency counts** for both `t` and the current window in `s`.
    - If the frequency count of the window matches `t`, it is an anagram.
    - Slide the window forward and update frequency counts.

    Time Complexity: O(N) where N is the length of `s` (each letter is processed once).
    Space Complexity: O(1) since we use fixed-size arrays for character frequencies.
    """

    len_s, len_t = len(s), len(t)
    
    # If `t` is longer than `s`, no anagram substrings are possible
    if len_t > len_s:
        return 0
    
    count = 0  # Stores the count of anagram substrings
    expected_freqs, window_freqs = [0] * 26, [0] * 26  # Frequency arrays for 'a' to 'z'

    # Step 1: Build the frequency map for `t`
    for c in t:
        expected_freqs[ord(c) - ord('a')] += 1  # Convert char to index and update count

    left = right = 0  # Pointers for the sliding window

    # Step 2: Iterate through `s` with a sliding window of size `len_t`
    while right < len_s:
        # Add the current character to the window frequency
        window_freqs[ord(s[right]) - ord('a')] += 1

        # If window size matches `len_t`, check for anagram
        if right - left + 1 == len_t:
            if window_freqs == expected_freqs:
                count += 1  # Found an anagram

            # Remove the leftmost character to slide the window
            window_freqs[ord(s[left]) - ord('a')] -= 1
            left += 1  # Move left pointer forward

        # Expand the window by moving right pointer
        right += 1
    
    return count  # Return total count of anagram substrings
