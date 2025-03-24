'''
https://leetcode.com/problems/continuous-subarray-sum/description/

✅ Why Index -1?
This is a trick to handle subarrays starting from index 0.

Let’s say:

python
Copy
Edit
nums = [6, 1, 2], k = 6
The cumulative sum at index 0 is:

python
Copy
Edit
total = 6 → 6 % 6 = 0
So at index 0, remainder is 0.

Now check:

python
Copy
Edit
i - remainder[0] = 0 - (-1) = 1  ❌ (length < 2)
But by index 2:

sum = 6 + 1 + 2 = 9

9 % 6 = 3 → still no match

Now if another 3 appears later, it’ll check if a subarray of length ≥ 2 had the same remainder before.

So storing remainder 0 at index -1 ensures that:

Any subarray starting at index 0 is still valid

The length check still works: i - (-1) = i + 1, which is the full length from index 0 to i
'''
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the first occurrence of a remainder
        remainder = {0: -1}  # Initialize with remainder 0 at index -1 to handle edge cases where first element itself is multiple of k
        total = 0  # Variable to maintain the cumulative sum

        # Iterate through the array
        for i, n in enumerate(nums):
            total += n  # Update cumulative sum
            
            # Compute remainder of total sum when divided by k
            r = total % k

            # If this remainder has never been seen before, store the index
            if r not in remainder:
                remainder[r] = i  # Store first occurrence of this remainder
            
            # If we have seen this remainder before and the subarray size is at least 2
            if i - remainder[r] > 1:
                return True  # Found a valid subarray
            
        # If no valid subarray found, return False
        return False
