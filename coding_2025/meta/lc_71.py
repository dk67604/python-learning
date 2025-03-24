'''
https://leetcode.com/problems/simplify-path/

Time Complexity: O(n), where n is the length of the input string path.

Explanation:

Splitting the string by '/' takes O(n) time.

Iterating through each token and performing operations (push/pop) on the stack takes O(n) in total because each directory name is processed at most once.

Joining the stack to form the result also takes O(n) in the worst case.

So, the overall time complexity is O(n).

Space Complexity: O(n)

Explanation:

In the worst case, all parts of the path are valid directory names and get stored in the stack, which takes O(n) space.

The final output string (resulting simplified path) also requires O(n) space to store.
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
