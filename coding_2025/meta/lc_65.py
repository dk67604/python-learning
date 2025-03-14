'''
Algorithm

Now that we have laid out the rules, let's iterate over the input. For each character, determine what group it belongs to, and verify that it follows the rules.

Declare 3 variables seenDigit, seenExponent, and seenDot. Set all of them to false.

Iterate over the input.

If the character is a digit, set seenDigit = true.

If the character is a sign, check if it is either the first character of the input, or if the character before it is an exponent. If not, return false.

If the character is an exponent, first check if we have already seen an exponent or if we have not yet seen a digit. If either is true, then return false. Otherwise, set seenExponent = true, and seenDigit = false. We need to reset seenDigit because after an exponent, we must construct a new integer.

If the character is a dot, first check if we have already seen either a dot or an exponent. If so, return false. Otherwise, set seenDot = true.

If the character is anything else, return false.

At the end, return seenDigit. This is one reason why we have to reset seenDigit after seeing an exponent - otherwise an input like "21e" would be incorrectly judged as valid.
https://leetcode.com/problems/valid-number/
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        # Flags to track occurrences of digits, exponent, and decimal point
        digitSeen, exponentSeen, dotSeen = False, False, False
        
        for i, c in enumerate(s):
            if c in ['e', 'E']:  # Check if the character is an exponent
                # Exponent should appear only once and must be preceded by a number
                if exponentSeen or not digitSeen:
                    return False
                exponentSeen = True  # Mark that an exponent has been seen
                digitSeen = False  # Reset digitSeen because there must be digits after 'e' or 'E'

            elif c == '.':  # Check if the character is a decimal point
                # A decimal point cannot appear after an exponent and should appear only once
                if dotSeen or exponentSeen:
                    return False
                dotSeen = True  # Mark that a decimal point has been seen

            elif c in ['+', '-']:  # Check if the character is a sign ('+' or '-')
                # The sign should appear only at the beginning or right after an exponent
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False

            elif c.isdigit():  # If the character is a digit
                digitSeen = True  # Mark that a digit has been seen

            else:  # If an invalid character is encountered
                return False

        # A valid number must contain at least one digit
        return digitSeen
