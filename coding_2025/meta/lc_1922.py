class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n % 2 == 0:
            ne = n // 2
        else:
            ne = (n + 1) //2
        no = n // 2
        te = pow(5, ne, MOD)
        tp = pow(4,no, MOD)
        return (tp*te) % MOD