'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
'''

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right = 0, 0  # Sliding window boundaries
        char_freq = defaultdict(int)  # Frequency map of characters in the current window
        maxLen = 0  # Track the length of the longest valid substring

        # Expand the window to the right
        while right < len(s):
            right_char = s[right]
            char_freq[right_char] += 1  # Add current character to frequency map

            # Shrink the window from the left if we exceed k distinct characters
            while len(char_freq) > k:
                left_char = s[left]
                char_freq[left_char] -= 1  # Reduce count of the leftmost character
                if char_freq[left_char] == 0:
                    del char_freq[left_char]  # Remove it from map if frequency is 0
                left += 1  # Move the left boundary forward

            # Update maxLen if the current window is longer
            maxLen = max(maxLen, right - left + 1)
            right += 1  # Expand the right boundary

        return maxLen  # Return the maximum length found
