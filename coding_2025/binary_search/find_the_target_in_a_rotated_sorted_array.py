class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for target in a rotated sorted array and returns its index if found, else -1.
        Uses binary search logic with O(log n) time complexity.
        """

        left, right = 0, len(nums) - 1

        # Continue searching while the window is valid
        while left < right:
            mid = (left + right) // 2

            # Found the target at the mid
            if nums[mid] == target:
                return mid

            # Check if the left half [left ... mid] is sorted
            if nums[left] <= nums[mid]:
                # If target is within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # search in the left half
                else:
                    left = mid + 1   # search in the right half

            # Else, the right half [mid ... right] is sorted
            else:
                # If target is within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # search in the right half
                else:
                    right = mid - 1  # search in the left half

        # Final check when left == right
        return left if nums and nums[left] == target else -1
