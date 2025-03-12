'''
1249. Minimum Remove to Make Valid Parentheses
Solved
Medium
Topics
Companies
Hint
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Given a string `s` containing letters and parentheses, remove the 
        minimum number of parentheses to make the string valid.
        
        A valid string means that:
        - Open '(' parentheses must have a corresponding closing ')' parentheses.
        - Parentheses must be properly nested.
        """
        
        # Stack to store indices of unmatched '(' parentheses
        extraParentheses = []
        
        # Convert string to list to modify characters easily
        s = list(s)
        
        # First pass: Identify invalid ')' parentheses
        for index, ch in enumerate(s):
            if ch == '(':
                # Store index of '(' for future matching
                extraParentheses.append(index)
            elif ch == ')':
                if extraParentheses:
                    # Valid pair found, remove matched '(' from stack
                    extraParentheses.pop()
                else:
                    # No matching '(', mark ')' for removal
                    s[index] = ''

        # Second pass: Remove unmatched '(' parentheses
        while extraParentheses:
            s[extraParentheses.pop()] = ''

        # Return the final valid string
        return ''.join(s)
