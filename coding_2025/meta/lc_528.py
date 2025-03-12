'''
528. Random Pick with Weight
Medium
Topics
Companies
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
 

Example 1:

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
Example 2:

Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
 

Constraints:

1 <= w.length <= 104
1 <= w[i] <= 105
pickIndex will be called at most 104 times.
'''
import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        """
        Preprocessing step to convert the given weights into a prefix sum 
        of probabilities, effectively creating a probability distribution.
        """
        self.w = w  # Store the weights list

        # Step 1: Calculate the total sum of weights
        denom = sum(self.w)

        # Step 2: Normalize the weights by converting them into probabilities
        for i in range(len(self.w)):
            self.w[i] = self.w[i] / denom  # Convert each weight into a fraction of total weight

        # Step 3: Convert the probabilities into a cumulative sum (prefix sum)
        # This helps in determining the region each index occupies on a [0,1] range.
        for i in range(1, len(self.w)):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        """
        Picks an index randomly based on weight distribution using a random
        number in the range [0,1] and checking where it falls in the cumulative sum.
        """
        # Generate a random number in the range [0,1]
        N = random.uniform(0, 1)

        # Initialize index and a flag for breaking the loop
        flag = 1
        index = -1

        # Iterate through the cumulative probability array to find the corresponding index
        while flag:
            index += 1

            # If N falls within the cumulative probability range, return the corresponding index
            if N <= self.w[index]:
                flag = 0  # Exit loop

        return index



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()