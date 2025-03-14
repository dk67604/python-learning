'''
https://leetcode.com/problems/dot-product-of-two-sparse-vectors/description/
'''

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Initializes a sparse vector from a given list of integers.
        
        Instead of storing all elements, we store only the non-zero elements
        in a dictionary (`self.nums`), where:
        - Key: Index of the non-zero element
        - Value: The non-zero element itself

        This optimizes space complexity by ignoring zero elements.

        Time Complexity: O(N) where N is the length of `nums`
        Space Complexity: O(K) where K is the number of non-zero elements
        """
        self.nums = {i: n for i, n in enumerate(nums) if n}  # Store only non-zero elements

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Computes the dot product of two sparse vectors efficiently.

        The dot product formula is:
            dot_product = sum(A[i] * B[i]) for all i

        Since most values in a sparse vector are zero, we only multiply 
        the non-zero elements that exist in both vectors.

        Approach:
        - Iterate over the smaller dictionary (for efficiency).
        - Multiply matching indices from both dictionaries.
        - Sum up the products.

        Time Complexity: O(K1 + K2) where K1, K2 are the non-zero elements in each vector.
        Space Complexity: O(1) (no extra space used)
        
        Args:
            vec (SparseVector): Another sparse vector.

        Returns:
            int: The dot product of the two vectors.
        """
        result = 0  # Store the final dot product

        # Optimize by iterating over the smaller dictionary for efficiency
        if len(self.nums) < len(vec.nums):
            smaller, larger = self.nums, vec.nums
        else:
            smaller, larger = vec.nums, self.nums

        # Compute dot product only for indices that exist in both vectors
        for key in smaller.keys():
            if key in larger:  # If index exists in both vectors
                result += smaller[key] * larger[key]

        return result  # Return the computed dot product

# Usage example:
# v1 = SparseVector([1, 0, 0, 2, 3])
# v2 = SparseVector([0, 3, 0, 4, 0])
# ans = v1.dotProduct(v2)  # Expected output: 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
