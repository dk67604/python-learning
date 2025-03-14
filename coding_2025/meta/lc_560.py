'''
https://leetcode.com/problems/subarray-sum-equals-k/
'''
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Counter for the number of subarrays that sum to `k`
        count = 0  
        
        # Dictionary to store the frequency of prefix sums
        prefix_sum_map = {0: 1}  # Initialize with sum 0 to handle cases where subarray starts at index 0
        
        # Variable to store the current prefix sum
        curr_prefix_sum = 0  
        
        # Iterate through the array to calculate prefix sums
        for num in nums:
            curr_prefix_sum += num  # Update the running prefix sum
            
            # Check if there exists a subarray that sums to `k`
            # A subarray sum is valid if (curr_prefix_sum - k) was seen before
            if curr_prefix_sum - k in prefix_sum_map:
                count += prefix_sum_map[curr_prefix_sum - k]  # Add the count of previous occurrences
            
            # Update prefix_sum_map with the current prefix sum
            # This keeps track of how many times each prefix sum appears
            prefix_sum_map[curr_prefix_sum] = prefix_sum_map.get(curr_prefix_sum, 0) + 1  
        
        # Return the total count of valid subarrays
        return count
