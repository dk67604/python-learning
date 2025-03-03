class Solution:
    def isValid(self, s: str) -> bool:
        parentheses_map = {'(':')', '{':'}', 
        '[':']'}
        stack = []
        for c in s:
            if c in parentheses_map:
                stack.append(c)
            else:
                if stack and parentheses_map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack        