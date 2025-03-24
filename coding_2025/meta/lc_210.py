'''
https://leetcode.com/problems/course-schedule-ii/description/

✅ Time Complexity: O(n + p)
Where:

n is the number of courses,

p is the number of prerequisite pairs.

Explanation:
Graph Construction:

Looping through p prerequisite pairs to build the adjacency list and in_degrees array → O(p)

Queue Initialization:

Iterating through all n courses to enqueue those with zero in-degree → O(n)

Topological Sort Processing:

Each node (course) is dequeued at most once → O(n)

For each node, you loop over its neighbors (edges), and across all nodes, you process all p edges once → O(p)

So total time complexity = O(n + p)

✅ Space Complexity: O(n + p)
Explanation:

Adjacency list (graph) stores p edges → O(p)

In-degree array stores n values → O(n)

Queue can hold up to n elements → O(n)

Result list (course_order) stores up to n elements → O(n)

So total space complexity = O(n + p)

'''
from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Returns the order in which courses should be taken to complete all courses.
        Uses **Topological Sorting (Kahn's Algorithm)** to find a valid order.
        If it is not possible to complete all courses (cycle detected), return an empty list.
        
        :param n: Number of courses (0 to n-1).
        :param prerequisites: List of prerequisite pairs [course, prerequisite] 
                              meaning "To take `course`, you must first complete `prerequisite`".
        :return: A list representing the order of courses, or an empty list if not possible.
        """

        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)  # Adjacency list representation
        in_degrees = [0] * n  # Track number of prerequisites for each course

        # Step 2: Populate the graph and in-degree array
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)  # prerequisite → course (correct direction)
            in_degrees[course] += 1  # Increment in-degree of `course`
        
        # Step 3: Initialize the queue with courses that have no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:  # No prerequisites, can take immediately
                queue.append(i)
        
        # Step 4: Process courses in topological order
        course_order = []  # Store the order in which courses should be taken

        while queue:
            node = queue.popleft()  # Take a course with no prerequisites
            course_order.append(node)  # Append course to order list

            # Reduce the in-degree of dependent courses
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1  # Remove the prerequisite requirement

                # If a dependent course now has no prerequisites, add it to the queue
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If all courses are processed, return the order. Otherwise, return an empty list (cycle detected).
        return course_order if len(course_order) == n else []
