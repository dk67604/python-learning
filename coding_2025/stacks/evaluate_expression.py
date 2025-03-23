def evaluate_expression(s: str) -> int:
    """
    Evaluates a string expression containing integers, '+', '-', and parentheses.
    Supports nested expressions like: "1 + (2 - (3 + 4))"

    :param s: A string expression
    :return: Integer result of the evaluated expression
    """

    stack = []             # Stack to store intermediate results and signs
    curr_num = 0           # Current number being built from digits
    sign = 1               # Current sign: 1 for '+', -1 for '-'
    res = 0                # Ongoing result of the expression

    for c in s:
        if c.isdigit():
            # Build the current number digit by digit
            curr_num = 10 * curr_num + int(c)

        elif c == '+' or c == '-':
            # Apply the previous number with its sign to the result
            res += curr_num * sign

            # Update sign for next number
            sign = -1 if c == '-' else 1

            # Reset current number
            curr_num = 0

        elif c == '(':
            # Push current result and sign to stack to evaluate nested expression
            stack.append(res)
            stack.append(sign)

            # Reset result and sign for the new sub-expression
            res, sign = 0, 1

        elif c == ')':
            # Finalize current sub-expression
            res += curr_num * sign

            # Multiply by the sign before the parenthesis
            res *= stack.pop()

            # Add to the result calculated before the parenthesis
            res += stack.pop()

            # Reset current number
            curr_num = 0

    # Add the last number (if any) to the result
    return res + curr_num * sign
