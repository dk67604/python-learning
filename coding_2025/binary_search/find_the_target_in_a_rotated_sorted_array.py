class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Here the idea is take rotation into consideration that will result in searching
        # the target element in O(log(n)) time instead linear time
        # To acheive this task after finding mid point we try to see which part of the subarray
        # is sorted and then  try to find the target element in that and adjust the position of left
        # and right 
        left , right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            # if the left subarraya [left: mid] is sorted, check if the target
            # falls in this range. If it does search the left subarray, search the right
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return left if nums and nums[left] == target else -1 
        