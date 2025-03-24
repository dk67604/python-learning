'''
https://leetcode.com/problems/basic-calculator-ii/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

✅ Time Complexity: O(n), where n is the length of the input string s.
Explanation:

You loop through the entire string exactly once → O(n)

Each number and operator is processed once.

Stack operations (append, pop) are O(1) each.

Final sum(stack) runs in O(n) time (in the worst case, every digit forms a new number).

So overall:
O(n)

✅ Space Complexity: O(n) in the worst case.
Explanation:

The stack stores intermediate results.

In the worst case (e.g., only additions/subtractions), you push up to n values onto the stack → O(n) space.

currentNumber, operation, and loop variables take constant space.
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
