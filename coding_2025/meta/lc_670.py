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
