def msis(nums: list):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]
    maxSum = nums[0]
    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
        maxSum = max(maxSum, dp[i])
    return maxSum


if __name__ == '__main__':
    print(msis([4, 1, 2, 6, 10, 1, 12]))
    print(msis([-4, 10, 3, 7, 15]))
