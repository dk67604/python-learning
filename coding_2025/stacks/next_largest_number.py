from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    """
    For each element in the list, finds the next greater number to its right.
    If no such element exists, return -1 for that position.

    :param nums: List of integers
    :return: List of next greater elements
    """

    res = [0] * len(nums)    # Result array
    stack = []               # Stack to keep track of "next greater candidates"

    # Traverse the list from right to left
    for i in range(len(nums) - 1, -1, -1):

        # Pop elements from stack that are smaller than or equal to current number
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # If stack is not empty, the top is the next greater element
        res[i] = stack[-1] if stack else -1

        # Push the current number to stack as potential greater for the next element to the left
        stack.append(nums[i])  # ❗ Fixed: originally used nums[-1] which is wrong

    return res
