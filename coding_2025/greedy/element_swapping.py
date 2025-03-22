'''
Element Swapping
Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
Signature
int[] findMinArray(int[] arr, int k)
Input
n is in the range [1, 1000].
Each element of arr is in the range [1, 1,000,000].
k is in the range [1, 1000].
Output
Return an array of n integers output, the lexicographically smallest sequence achievable after at most k swaps.
Example 1
n = 3
k = 2
arr = [5, 3, 1]
output = [1, 5, 3]
We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
Example 2
n = 5
k = 3
arr = [8, 9, 11, 2, 1]
output = [2, 8, 9, 11, 1]
We can swap [11, 2], followed by [9, 2], then [8, 2].

'''

from typing import List

def findMinArray(arr: List[int], k: int):
    n = len(arr)

    for i in range(n):
        pos = i  # Initialize the current position as the smallest

        # Look ahead up to k steps to find the smallest number in the window [i+1, i+k]
        for j in range(i + 1, min(n, i + k + 1)):
            # If a smaller number is found, update its position
            if arr[j] < arr[pos]:
                pos = j

        num_swaps = pos - i  # Number of adjacent swaps needed to bring arr[pos] to position i

        if num_swaps > k:
            continue  # Skip if we can't afford these swaps

        # Perform adjacent swaps to bring the smallest number to position i
        for j in range(pos, i, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

        k -= num_swaps  # Decrease remaining swap budget

        if k == 0:
            break  # Stop if no swaps left

    return arr
