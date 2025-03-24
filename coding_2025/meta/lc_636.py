'''
https://leetcode.com/problems/exclusive-time-of-functions/description/
'''

from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n                # Result array to store exclusive time for each function ID
        stack = []                   # Stack to keep track of currently running functions
        prev = 0                     # Keeps the timestamp of the last processed log

        for log in logs:
            # Split the log into function ID, type ("start"/"end"), and timestamp
            fn_id, typ, time = log.split(':')
            fn_id, time = int(fn_id), int(time)

            if typ == "start":
                # If there's already a running function on top of the stack,
                # calculate how much time it ran until this new function started
                if stack:
                    # Add the elapsed time since prev to the current running function
                    res[stack[-1]] += time - prev

                # Push the new function onto the stack (start running it)
                stack.append(fn_id)
                prev = time  # Update prev to current start time

            else:  # typ == "end"
                # The function at the top of the stack ends now
                last_fn_id = stack.pop()

                # Add the time this function was running to its result
                # (from prev to current time, inclusive → +1)
                res[last_fn_id] += time - prev + 1

                # Update prev to time just after this function ends
                prev = time + 1

        return res
