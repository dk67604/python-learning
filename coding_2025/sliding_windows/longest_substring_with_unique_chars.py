def longest_substring_with_unique_chars(s: str) -> int:
    """
    Given a string `s`, find the length of the longest substring 
    without repeating characters.

    Approach:
    - Use the **Sliding Window** technique to maintain a valid substring.
    - Use a **HashMap (`prev_indexes`)** to track the last seen index of each character.
    - Expand the window with `right` pointer.
    - If a repeating character is found, **shrink the window (`left`)** to exclude the duplicate.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    
    max_len = 0  # Stores the maximum length of a unique-character substring
    prev_indexes = {}  # Dictionary to store the last seen index of each character
    left = right = 0  # Pointers for the sliding window

    # Step 1: Traverse the string with a sliding window
    while right < len(s):
        # Step 2: If character at `right` is a duplicate within the window
        if (s[right] in prev_indexes) and left <= prev_indexes[s[right]]:
            # Move `left` pointer to the right of the last occurrence of `s[right]`
            left = prev_indexes[s[right]] + 1

        # Step 3: Update the maximum length encountered so far
        max_len = max(max_len, right - left + 1)

        # Step 4: Store/update the last seen index of the character
        prev_indexes[s[right]] = right

        # Step 5: Expand the window by moving `right`
        right += 1
    
    # Step 6: Return the maximum length of unique-character substring
    return max_len
