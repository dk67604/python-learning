'''
https://leetcode.com/problems/maximum-swap/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        """
        Finds the maximum number that can be obtained by swapping two digits at most once.

        :param num: An integer
        :return: The maximum possible number after at most one swap
        """

        # Convert the integer to a list of characters (digits)
        nums = list(str(num))
        n = len(nums)

        # Array to store the index of the maximum digit to the right for each position
        max_right_index = [0] * n  
        max_right_index[n-1] = n-1  # The last digit is the maximum in its position

        # Populate max_right_index with the rightmost max digit for each position
        for i in range(n-2, -1, -1):
            # Store the index of the max digit on the right (or itself if it's larger)
            max_right_index[i] = i if nums[i] > nums[max_right_index[i+1]] else max_right_index[i+1]
        
        # Iterate through the digits and find the first instance where a swap improves the number
        for i in range(n):
            if nums[i] < nums[max_right_index[i]]:  # If a larger digit exists to the right
                # Swap the current digit with the rightmost maximum digit
                nums[i], nums[max_right_index[i]] = nums[max_right_index[i]], nums[i]
                return int(''.join(nums))  # Convert back to integer and return
        
        # If no swap was made, return the original number
        return num
