'''
https://leetcode.com/problems/exclusive-time-of-functions/description/
'''

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n                # Stores exclusive time for each function
        stack = []                   # Stack to track currently running functions
        prev = 0                     # Previous timestamp

        for log in logs:
            fn_id, typ, time = log.split(':')
            fn_id, time = int(fn_id), int(time)

            if typ == "start":
                if stack:
                    # Add time to the function at the top of the stack
                    res[stack[-1]] += time - prev
                stack.append(fn_id)
                prev = time  # Update prev to the start time of new function
            else:  # "end"
                res[stack.pop()] += time - prev + 1
                prev = time + 1  # Update prev to the time after current function ends

        return res
