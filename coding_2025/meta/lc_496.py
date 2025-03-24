'''
496. Next Greater Element I
Solved
Easy
Topics
Companies
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

Constraints:

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
 

Follow up: Could you find an O(nums1.length + nums2.length) solution?

✅ Time Complexity: O(m + n)
Where:

m = len(nums1)

n = len(nums2)

🔍 Step-by-step Breakdown:
Preprocessing nums2 with a stack: O(n)

python
Copy
Edit
for num in reversed(nums2):
Each element is pushed and popped at most once from the stack.

So even with the while stack: inside, the total work is linear in nums2.

The hashmap is filled with at most n entries — constant-time operations.

Building output for nums1: O(m)

python
Copy
Edit
for j in nums1:
    output.append(hashmap[j])
Each lookup in the hashmap is O(1).

✅ Total Time:
text
Copy
Edit
O(n) + O(m) = O(m + n)
✅ Space Complexity: O(n)
Stack: Can hold up to n elements → O(n)

Hashmap: Stores one mapping for each number in nums2 → O(n)

Output: Stores m results → O(m), but since it's returned, it's not counted as extra space.
'''
from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Stack to keep track of next greater elements in nums2
        stack = []
        # Hashmap to store the next greater element for each number in nums2
        hashmap = {}
        # Output list to store the results for elements in nums1
        output = []

        # Iterate through nums2 in reverse order (right to left)
        for num in reversed(nums2):
            # Maintain a decreasing stack (pop elements smaller than current number)
            while stack:
                if stack[-1] > num:
                    # Store the next greater element in the hashmap
                    hashmap[num] = stack[-1]
                    # Push the current number onto the stack
                    stack.append(num)
                    break
                else:
                    # Pop smaller elements since they won't be needed anymore
                    stack.pop()
            
            # If stack is empty (no greater element found), store -1
            if not stack:
                hashmap[num] = -1
                stack.append(num)

        # Iterate over nums1 to retrieve results from the hashmap
        for j in nums1:
            output.append(hashmap[j])

        return output
