'''
https://leetcode.com/problems/construct-binary-tree-from-string/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:

        def getNumber(index: int) -> (int, int):
            """
            Helper function to parse a number (including negative).
            Returns the parsed number and updated index.
            """
            is_negative = False
            if s[index] == '-':
                is_negative = True
                index += 1

            number = 0
            while index < len(s) and s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1

            return -number if is_negative else number, index

        if not s:
            return None  # Empty string → no tree

        root = TreeNode()  # Initially create a dummy root node
        stack = [root]     # Stack to track current processing nodes

        index = 0
        while index < len(s):
            node = stack.pop()  # Get current node from stack to process

            # Case 1: Current char is a digit or negative sign → parse number
            if s[index].isdigit() or s[index] == '-':
                value, index = getNumber(index)  # Parse the value
                node.val = value                 # Assign value to the current node

                # If more data exists and next char is '(', a left child starts
                if index < len(s) and s[index] == '(':
                    stack.append(node)              # Push current node back to stack
                    node.left = TreeNode()          # Prepare left child node
                    stack.append(node.left)         # Add left child to stack for further parsing

            # Case 2: Left child already filled, and next is '(' → begin right child
            elif node.left and s[index] == '(':
                stack.append(node)                  # Push current node back
                node.right = TreeNode()             # Prepare right child node
                stack.append(node.right)            # Add right child to stack

            index += 1  # Move to next character This next character could ')'

        # At the end, either stack has one last parent to return, or return root
        return stack.pop() if stack else root
