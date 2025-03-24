'''
https://leetcode.com/problems/word-break/description/

✅ Time Complexity: O(n²), where n is the length of the input string s.

Explanation:

For each index start in the queue (at most n different positions), you may check up to n - start substrings by varying end from start + 1 to n.

Checking if s[start:end] is in the dictionary takes O(1) (thanks to the set).

Since each end index is processed only once (due to seen), the total number of substring checks is bounded by O(n²).

✅ Space Complexity: O(n + m), where:

n is the length of the input string s,

m is the total number of characters in wordDict.

Explanation:

words set takes O(m) space to store the dictionary.

queue and seen sets can store up to n indices → O(n).

No extra space proportional to substrings or a DP table is used.

🧠 Summary:
Time: O(n²)

Space: O(n + m)
'''
from typing import List
from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into a sequence of one or more dictionary words.
        Uses BFS to explore all valid segmentations.
        """

        words = set(wordDict)       # Convert wordDict to set for O(1) lookup
        queue = deque([0])          # BFS queue holds starting indices to explore
        seen = set()                # Tracks visited indices to prevent re-processing

        while queue:
            start = queue.popleft()  # Get the current start index to explore from

            if start == len(s):      # Reached the end of the string with valid segmentations
                return True

            # Try every possible substring starting from `start`
            for end in range(start + 1, len(s) + 1):
                # Skip if we've already visited this end position
                if end in seen:
                    continue

                # If substring from start to end exists in dictionary
                if s[start:end] in words:
                    queue.append(end)   # Add new start index to queue
                    seen.add(end)       # Mark end index as visited

        # If we've explored all options and found no valid break
        return False
