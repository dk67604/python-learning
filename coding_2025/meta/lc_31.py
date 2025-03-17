'''
https://leetcode.com/problems/next-permutation/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modifies the list 'nums' in-place to produce the next lexicographical permutation.
        If no such permutation exists (i.e., the list is in descending order), it transforms into the lowest possible order.

        :param nums: List of integers representing a permutation.
        :return: None (modifies 'nums' in-place).
        """
        
        n = len(nums)
        i = n - 2  # Start from the second last element
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i+1] <= nums[i]:  
            i -= 1  # Keep moving left while the sequence is non-increasing
        
        if i >= 0:  # If a decreasing element was found
            j = n - 1  # Start from the last element
            
            # Step 2: Find the first element larger than nums[i] from the right
            while nums[j] <= nums[i]:
                j -= 1  
            
            # Step 3: Swap nums[i] and nums[j] to get the next larger permutation
            nums[i], nums[j] = nums[j], nums[i]  
        
        # Step 4: Reverse the sequence after index 'i' to get the next lexicographical order
        self.reverse(nums, i + 1)

    def reverse(self, nums: List[int], start: int) -> None:
        """
        Reverses the sublist nums[start:] in-place.

        :param nums: List of numbers.
        :param start: Starting index of the sublist to reverse.
        :return: None (modifies 'nums' in-place).
        """
        i, j = start, len(nums) - 1  # Start and end pointers
        
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]  # Swap elements
            i += 1
            j -= 1
