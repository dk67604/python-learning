'''
https://leetcode.com/problems/next-permutation/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days

Time Complexity: O(n), where n is the length of the list nums.

Explanation:

Step 1: Scanning from right to left to find the first decreasing element takes at most O(n).

Step 2: Finding the next larger element to swap also takes at most O(n).

Step 3: Swapping two elements takes O(1).

Step 4: Reversing the sublist takes at most O(n).

All steps together are linear in time, so the total time complexity is O(n).

Space Complexity: O(1)

The algorithm modifies the input list in place and uses only a constant amount of extra space.
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
