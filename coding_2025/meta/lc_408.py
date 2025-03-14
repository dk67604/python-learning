'''
408. Valid Word Abbreviation
Solved
Easy
Topics
Companies
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # Pointers for `word` and `abbr`
        
        # Iterate through both `word` and `abbr`
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():  # If the current character in `abbr` is a digit
                if abbr[j] == '0':  
                    # Leading zeros are not allowed in a valid abbreviation
                    return False
                
                shift = 0  # Stores the number to skip characters in `word`
                
                # Build the full number (handling multi-digit numbers)
                while j < len(abbr) and abbr[j].isdigit():
                    shift = (shift * 10) + int(abbr[j])  # Convert string to integer
                    j += 1  # Move to the next character in `abbr`
                
                i += shift  # Skip `shift` number of characters in `word`
            
            else:  # If `abbr[j]` is a letter
                if i >= len(word) or word[i] != abbr[j]:  
                    # Mismatch in characters or out of bounds, return False
                    return False
                
                i += 1  # Move to the next character in `word`
                j += 1  # Move to the next character in `abbr`
        
        # Both `word` and `abbr` should
