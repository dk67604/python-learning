'''
https://leetcode.com/problems/powx-n/description/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # Recursive helper function to compute x^n efficiently
        def helper(x, n):
            # Base case: If x is 0, any power of 0 is 0 (except 0^0 which is typically defined as 1)
            if x == 0: 
                return 0
            # Base case: Any number raised to the power 0 is 1
            if n == 0:
                return 1
            
            # Recursive divide-and-conquer: Compute power for n//2
            res = helper(x, n // 2)
            
            # Multiply result by itself (x^(n//2) * x^(n//2))
            res = res * res
            
            # If `n` is odd, multiply once more by `x`
            return x * res if n % 2 == 1 else res
        
        # Compute power using the absolute value of `n`
        ans = helper(x, abs(n))
        
        # If `n` is negative, take reciprocal of the result
        return ans if n >= 0 else 1 / ans
