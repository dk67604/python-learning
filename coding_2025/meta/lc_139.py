'''
https://leetcode.com/problems/word-break/description/
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
