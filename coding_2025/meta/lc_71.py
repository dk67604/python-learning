'''
https://leetcode.com/problems/simplify-path/
'''
from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        tokens = path.split('/')
        for token in tokens:
            if stack and token == '..':
                stack.pop()
            elif not token == "" and not token == '.' and not token == '..':
                stack.append(token)

        if not stack:
            return '/'
        return '/' + '/'.join(stack)