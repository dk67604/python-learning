'''
https://leetcode.com/problems/custom-sort-string/description/
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Given a custom character order `order` and a string `s`, reorder `s`
        such that characters appear in the order given in `order`. 
        Characters not present in `order` should appear at the end in any order.
        
        Approach:
        - Use a frequency map to count occurrences of characters in `s`.
        - Construct the result string by following the order in `order`.
        - Append remaining characters from `s` that are not in `order`.

        Time Complexity: O(N + M), where N is the length of `s` and M is the length of `order`.
        Space Complexity: O(N) for the frequency map.
        """

        # Step 1: Build frequency map for characters in `s`
        s_freq_map = {}  # Dictionary to store character counts in `s`
        for c in s:
            s_freq_map[c] = s_freq_map.get(c, 0) + 1  # Count occurrences

        result = ''  # Result string to store sorted characters

        # Step 2: Add characters in the order specified by `order`
        for char in order:
            if char in s_freq_map:  # If character exists in `s`
                result += char * s_freq_map[char]  # Append it repeated by its count
                del s_freq_map[char]  # Remove it from the map

        # Step 3: Append remaining characters that were not in `order`
        for k, v in s_freq_map.items():
            result += k * v  # Append remaining characters in any order

        return result  # Return the final sorted string
