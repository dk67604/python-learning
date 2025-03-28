'''
https://leetcode.com/problems/longest-repeating-character-replacement/
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}  # Dictionary to keep count of characters in the current window
        highest_freq = 0  # Highest frequency of a single character in the current window
        max_len = 0  # The length of the longest valid window found so far
        left = right = 0  # Sliding window pointers

        while right < len(s):
            # Expand the window by including the character at the 'right' pointer
            freqs[s[right]] = freqs.get(s[right], 0) + 1

            # Update the highest frequency character count seen in the current window
            highest_freq = max(highest_freq, freqs[s[right]])

            # Calculate how many characters need to be replaced to make all characters the same
            num_chars_to_replace = (right - left + 1) - highest_freq

            # If the number of replacements needed exceeds 'k', slide the window forward
            # by moving the left pointer to the right to maintain a valid window
            if num_chars_to_replace > k:
                # Decrease the count of the character at the left pointer as it's leaving the window
                freqs[s[left]] -= 1
                left += 1  

            # Update the maximum length of a valid window found so far
            max_len = max(max_len, right - left + 1)

            # Move the right pointer to expand the window
            right += 1

        return max_len
