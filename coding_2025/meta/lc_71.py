'''
https://leetcode.com/problems/simplify-path/
'''
from collections import deque

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a deque (stack) to store valid directory names
        stack = deque()
        
        # Split the path by '/' to get individual directory names or special symbols
        tokens = path.split('/')
        
        # Iterate through each token
        for token in tokens:
            if stack and token == '..':  
                # '..' means move up one directory, so pop from the stack if not empty
                stack.pop()
            elif not token == "" and not token == '.' and not token == '..':
                # If token is a valid directory name, push it onto the stack
                stack.append(token)

        # If the stack is empty, return root "/"
        if not stack:
            return '/'
        
        # Join the stack elements to form the final simplified path
        return '/' + '/'.join(stack)
