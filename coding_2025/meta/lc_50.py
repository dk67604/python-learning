'''
https://leetcode.com/problems/powx-n/description/

🧮 Why Is This Efficient?
Instead of multiplying x by itself n times (which would take O(n) time), this algorithm uses recursion to cut the problem in half each time, which gives us a logarithmic depth of computation.

⏱️ Time Complexity: O(log n)
The recursion depth is proportional to log₂(n) since n is halved on each call.

Each recursive step performs a constant amount of work (O(1)), so the total time complexity is O(log n).

🧠 Space Complexity: O(log n) (for recursive stack)
The recursion stack will go as deep as log₂(n) in the worst case, so the space complexity is also O(log n).
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


'''
Time Complexity : O(log n)
Space Complexity: O(1)
Say x = 2, n = 13 (binary: 1101)

We'll multiply:

2^1 (because the last bit is 1)

2^4 (because 3rd bit from right is 1)

2^8 (because 4th bit from right is 1)
'''
class Solution2:
    def myPow(self, x: float, n: int) -> float:
        # Handle negative exponents
        N = abs(n)
        result = 1.0
        current_product = x

        while N > 0:
            # If the current bit is set, multiply result
            if N % 2 == 1:
                result *= current_product
            
            # Square the base
            current_product *= current_product
            # Move to the next bit
            N //= 2
        
        # If original exponent was negative, take reciprocal
        return result if n >= 0 else 1 / result
