def evaluate_expression(s: str) -> int:
    stack = []
    curr_num, sign, res = 0, 1, 0
    for c in s:
        if c.isdigit():
            curr_num = 10*curr_num + int(c)
        # If current character is operator
        elif c == '+' or c == '-':
            res += curr_num * sign
            # Update the signe and curr_num
            sign = -1 if c == '-' else 1
            curr_num = 0
        elif c == '(':
            stack.append(res)
            stack.append(sign)
            res , sign = 0, 1
        elif c == ')':
            # Finalize the result of current nested expression
            res += sign * curr_num
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    return res + curr_num * sign
            

            