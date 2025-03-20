'''
https://leetcode.com/problems/task-scheduler/description/
'''

import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a list of CPU tasks and a cooldown period `n`,
        find the minimum time required to complete all tasks
        following the given constraints.
        """
        
        # Step 1: Count the frequency of each task
        count = Counter(tasks)  # Stores task frequencies
        
        # Step 2: Use a Max Heap (negate values to use Python's min-heap as a max-heap)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)  # Convert list into a heap
        
        # Step 3: Use a queue to track cooling tasks with their next available execution time
        queue = deque()  # Format: [remaining_count, next_available_time]
        
        time = 0  # Tracks the total time taken
        
        # Step 4: Process tasks using a heap and cooldown queue
        while maxHeap or queue:  # Continue until all tasks are completed
            time += 1  # Increment time at each step
            
            if maxHeap:  # If there are available tasks to process
                cnt = 1 + heapq.heappop(maxHeap)  # Process task (increment since we store negative counts)
                
                if cnt:  # If there are more instances of this task left
                    queue.append([cnt, time + n])  # Add it to cooldown queue with next available time
            
            # Step 5: If a task has finished its cooldown, reinsert it into the heap
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
                
        return time  # Return total time taken to complete all tasks
