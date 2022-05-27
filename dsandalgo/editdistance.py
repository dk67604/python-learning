# https://www.youtube.com/watch?v=We3YDTzNXEk
# https://leetcode.com/problems/edit-distance/

def min_edit_distance(word1, word2):
    r = len(word1)
    c = len(word2)
    dp = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(0, r + 1):
        for j in range(0, c + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[r][c]


if __name__ == '__main__':
    print(min_edit_distance("horse", "ros"))
