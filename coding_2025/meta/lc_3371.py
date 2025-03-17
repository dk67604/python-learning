'''
https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''

from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        Finds the largest outlier in the list.
        An outlier is defined as a number `num` such that removing `num` twice
        results in another number that already exists in the list.

        :param nums: List of integers
        :return: The largest valid outlier or float('-inf') if none exist.
        """
        
        # Step 1: Compute the total sum of all numbers
        total_sum = sum(nums)  

        # Step 2: Initialize variable to store the largest valid outlier
        largest_outlier = float('-inf')

        # Step 3: Build a frequency map to count occurrences of each number
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1  # Count each number
        
        # Step 4: Iterate through each unique number
        for num in freq_map.keys():
            # Compute the potential outlier using the formula:
            potential_outlier = total_sum - 2 * num  
            
            # Step 5: Check if potential_outlier exists in the frequency map
            if potential_outlier in freq_map:
                # Ensure validity:
                # - If potential_outlier is different from num, it's valid
                # - If potential_outlier == num, then num must appear at least twice
                if potential_outlier != num or freq_map[num] > 1:
                    # Corrected typo: Use largest_outlier instead of larget_outlier
                    largest_outlier = max(largest_outlier, potential_outlier)
        
        # Step 6: Return the largest outlier found (or -inf if none exist)
        return largest_outlier
