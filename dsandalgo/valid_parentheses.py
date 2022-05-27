from collections import deque


def is_valid(str1: str):
    stack = deque()

    for ch in str1:
        if ch == '(':
            stack.append(')')
        elif ch == '{':
            stack.append('}')
        elif ch == '[':
            stack.append(']')
        elif len(stack) == 0 or stack.pop() != ch:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid('()(){}['))
