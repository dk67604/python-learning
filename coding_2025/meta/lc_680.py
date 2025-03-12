'''
680. Valid Palindrome II
Solved
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = 1  # Maximum number of deletions allowed
        
        def verify(s: str, left, right, deleted):
            """
            Recursive function to check if a substring is a valid palindrome 
            with at most one deletion.
            """
            while left < right:
                if s[left] != s[right]:  # Mismatch found
                    if deleted == n:
                        return False  # Already deleted one character, cannot delete again
                    else:
                        # Try deleting either the left or right character and check if it's a palindrome
                        return verify(s, left+1, right, deleted+1) or verify(s, left, right-1, deleted+1)
                else:
                    # Continue checking next characters
                    left += 1
                    right -= 1
            return True  # If loop completes, it is a valid palindrome

        return verify(s, 0, len(s) - 1, 0)  # Start with the full string

# Iterative
class Solution2:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s, left, right):
            """Helper function to check if a substring is a palindrome"""
            while left < right:
                if s[left] != s[right]:
                    return False  # Mismatch found, not a palindrome
                left += 1
                right -= 1
            return True  # If loop completes, it is a palindrome

        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:  # Mismatch found
                # Try skipping one character (either left or right) and check if the rest is a palindrome
                return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        
        return True  # String is already a palindrome
