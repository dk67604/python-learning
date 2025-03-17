'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Computes the sum of all root-to-leaf numbers in a binary tree.
        
        Each root-to-leaf path represents a number formed by concatenating node values.
        The sum of all such numbers is returned.

        :param root: Root node of the binary tree
        :return: Sum of all root-to-leaf numbers
        """
        
        # Stack for iterative depth-first traversal (node, current number)
        stack = [(root, 0)]
        
        # Variable to store the sum of all root-to-leaf numbers
        root_to_leaf = 0 
        
        # Iterate using DFS (Depth-First Search)
        while stack:
            root, curr_number = stack.pop()  # Get the current node and its accumulated value
            
            if root is not None:
                # Update the current number by shifting left (multiplying by 10) and adding node value
                curr_number = curr_number * 10 + root.val

                # If it's a leaf node, add the current number to the total sum
                if root.left is None and root.right is None:
                    root_to_leaf += curr_number
                else:
                    # Push the right child first (so left is processed first in DFS order)
                    stack.append((root.right, curr_number))
                    stack.append((root.left, curr_number))

        return root_to_leaf  # Return the sum of all root-to-leaf numbers


class Solution2:
    def maximumSwap(self, num: int) -> int:
        """
        Finds the maximum number that can be obtained by swapping two digits at most once.

        :param num: An integer
        :return: The maximum possible number after at most one swap
        """

        # Convert the number to a list of digits (characters)
        nums = list(str(num))  

        # Variables to track the maximum digit seen from the right
        max_num = "0"  # Stores the maximum digit encountered (initialized to '0')
        max_i = -1  # Stores the index of the maximum digit encountered
        swap_i, swap_j = -1, -1  # Indices of digits to be swapped

        # Traverse the digits from right to left (reversed order)
        for i in reversed(range(len(nums))):
            if nums[i] > max_num:  # Update max_num and its index if a larger digit is found
                max_num = nums[i]
                max_i = i
            if nums[i] < max_num:  # If a smaller digit is found before max_num, mark it for swap
                swap_i, swap_j = i, max_i  

        # If a swap is possible, perform the swap
        if swap_i != -1:
            nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]  

        # Convert the list back to an integer and return
        return int(''.join(nums))
