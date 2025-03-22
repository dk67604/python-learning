'''
https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []               # Stack to store intermediate results
        currentNumber = 0        # Tracks the current number being parsed
        operation = '+'          # Default operation is addition

        for i, char in enumerate(s):
            # Build the current number if the character is a digit
            if char.isdigit():
                currentNumber = currentNumber * 10 + int(char)

            # If it's an operator (not digit and not space) or end of string
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                # Apply the last stored operation to currentNumber
                if operation == '+':
                    stack.append(currentNumber)  # Add to stack as is
                elif operation == '-':
                    stack.append(-currentNumber) # Push negative number
                elif operation == '*':
                    stack.append(stack.pop() * currentNumber)  # Multiply with top of stack
                elif operation == '/':
                    prev = stack.pop()
                    # Use int() to truncate towards zero (like Java's integer division)
                    stack.append(int(prev / currentNumber))

                # Update operation and reset current number for next round
                operation = char
                currentNumber = 0

        # Final result is the sum of all values in the stack
        return sum(stack)
