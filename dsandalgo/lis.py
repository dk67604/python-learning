def lis(nums: list):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return 1
    T = [1 for _ in range(n)]
    max_ans = 1
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] > nums[j]:
                if T[j] + 1 > T[i]:
                    T[i] = T[j] + 1
                    max_ans = max(max_ans, T[i])

    return max_ans


if __name__ == '__main__':
    print(lis([10, 9, 2, 5, 3, 7, 101, 18]))
