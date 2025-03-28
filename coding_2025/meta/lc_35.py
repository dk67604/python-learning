class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize the binary search boundaries
        left, right = 0, len(nums)  # Note: 'right' is exclusive

        # Perform binary search
        while left < right:
            # Find the middle index
            mid = (left + right) // 2

            # If the mid value is greater than or equal to target,
            # the target could be at mid or somewhere to the left
            if nums[mid] >= target:
                right = mid  # Shrink the search space to the left half (including mid)
            else:
                # If nums[mid] < target, the target must be to the right
                left = mid + 1  # Move left boundary to mid + 1

        # When loop exits, left == right and points to the correct insert position
        return left
