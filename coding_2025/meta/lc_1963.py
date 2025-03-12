'''
1963. Minimum Number of Swaps to Make the String Balanced
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
 

Constraints:

n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.
'''
class Solution:
    def minSwaps(self, s: str) -> int:
        """
        Given a string `s` consisting of '[' and ']', determine the minimum number 
        of adjacent swaps needed to make the brackets balanced.

        A balanced string means that for every opening bracket '[', there is a 
        corresponding closing bracket ']' in the correct order.

        Approach:
        - Use a stack to track unmatched '[' brackets.
        - Count the number of unpaired '[' brackets at the end.
        - The number of swaps needed to fix them is (unpaired_count + 1) // 2.

        Time Complexity: O(N)
        Space Complexity: O(N)
        """

        stack = []  # Stack to track unmatched '[' brackets

        # Step 1: Process the string to track unbalanced '[' brackets
        for c in s:
            if c == '[':
                # Push opening bracket to stack
                stack.append(c)
            elif stack and c == ']':
                # If there's a matching '[', remove it (balanced pair found)
                stack.pop()

        # Step 2: Compute the number of swaps needed
        # The remaining unpaired '[' count determines the number of swaps
        # Since each swap fixes 2 misplaced brackets, we use (len(stack) + 1) // 2
        return (len(stack) + 1) // 2
