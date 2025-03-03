def next_largets_number_to_the_right(nums: List[int]) -> List[int]:
    res = [0] * len(nums)
    stack = []
    for i in range(len(nums) -1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        res[i] = stack[-1] if stack else -1
        stack.append(nums[-1])

    return res