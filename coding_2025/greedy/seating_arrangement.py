'''
Seating Arrangements
There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i-1] inches.
The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table. As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent guests. Determine the minimum possible overall awkwardness of any seating arrangement.
Signature
int minOverallAwkwardness(int[] arr)
Input
n is in the range [3, 1000].
Each height arr[i] is in the range [1, 1000].
Output
Return the minimum achievable overall awkwardness of any seating arrangement.
Example
n = 4
arr = [5, 10, 6, 8]
output = 4
If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4. It's impossible to achieve a smaller overall awkwardness.
'''

from typing import List

def minOverallAwkwardness(arr: List[int]) -> int:
    # Step 1: Sort the array in **descending order**
    # We want to spread the largest elements as far apart as possible,
    # because big height differences between adjacent seats cause high awkwardness.
    arr.sort(reverse=True)

    n = len(arr)

    # Step 2: Place elements in a "pendulum" (zig-zag from center) fashion.
    # This helps distribute tall people apart to avoid sitting them next to each other.
    # Initialize an empty seating arrangement.
    seating = [0] * n

    # The largest person goes to the center.
    # Then we place alternately to the left and right of center.
    left = (n - 1) // 2  # Start just left of center for both even and odd n
    right = left + 1     # First position to the right of center
    idx = 0              # Index for descending sorted heights

    # Fill seats by alternating left and right from the center.
    while idx < n:
        if left >= 0:
            seating[left] = arr[idx]
            left -= 1
            idx += 1
        if idx < n and right < n:
            seating[right] = arr[idx]
            right += 1
            idx += 1

    # Step 3: Calculate maximum awkwardness (maximum absolute height difference
    # between all adjacent seated guests — including the circular wraparound).
    max_awkwardness = 0
    for i in range(n):
        diff = abs(seating[i] - seating[(i + 1) % n])  # Wraparound using modulo
        max_awkwardness = max(max_awkwardness, diff)

    return max_awkwardness
