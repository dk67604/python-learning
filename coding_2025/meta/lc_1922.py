class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        Given an integer `n`, count the number of "good" digit strings of length `n`.

        A "good" number:
        - Even indices (0-based) can be one of {0, 2, 4, 6, 8} (5 choices).
        - Odd indices (0-based) can be one of {2, 3, 5, 7} (4 choices).
        
        The task is to compute the total number of valid numbers of length `n` 
        under modulo `10^9 + 7`.
        """

        MOD = 10**9 + 7  # Large prime to prevent overflow
        
        # Step 1: Determine the count of even and odd positions
        if n % 2 == 0:
            ne = n // 2  # Number of even-indexed positions
        else:
            ne = (n + 1) // 2  # If odd length, there is one more even index than odd
        no = n // 2  # Number of odd-indexed positions

        # Step 2: Compute the total number of valid combinations
        # te = 5^ne (Choices for even-indexed positions)
        # tp = 4^no (Choices for odd-indexed positions)
        te = pow(5, ne, MOD)  # Fast modular exponentiation
        tp = pow(4, no, MOD)  # Fast modular exponentiation

        # Step 3: Compute the final result under modulo
        return (tp * te) % MOD  # Use modulo to prevent integer overflow
