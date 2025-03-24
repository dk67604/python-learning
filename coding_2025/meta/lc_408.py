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

🧠 Time and Space Complexity:
✅ Time Complexity: O(max(m, n))
m = length of word

n = length of abbr

You iterate through each character of abbr, and may also iterate over all characters in word.

In the worst case, each character in both strings is processed once → O(m + n) = O(max(m, n))

✅ Space Complexity: O(1)
Only a few pointers and variables are used.

No additional space is used that scales with input.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # Pointers for `word` and `abbr`

        # Iterate through both `word` and `abbr`
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():  # If the current character in `abbr` is a digit
                if abbr[j] == '0':  
                    # Leading zeros are not allowed
                    return False

                shift = 0  # Stores the number of characters to skip in `word`

                # Build the full number (handle multiple digits)
                while j < len(abbr) and abbr[j].isdigit():
                    shift = shift * 10 + int(abbr[j])
                    j += 1
                
                i += shift  # Skip `shift` characters in the word

            else:
                # If characters don't match or word is too short
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        # Ensure both pointers reach the end of their respective strings
        return i == len(word) and j == len(abbr)

