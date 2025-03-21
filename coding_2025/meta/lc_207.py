'''
https://leetcode.com/problems/course-schedule/description/
'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given the prerequisite dependencies.
        Uses **Topological Sorting (Kahn's Algorithm)** to detect cycles in a directed graph.
        
        :param n: Number of courses (0 to n-1).
        :param prerequisites: List of prerequisite pairs [a, b] meaning "To take `b`, you must first complete `a`".
        :return: True if all courses can be completed, otherwise False.
        """

        # Step 1: Build the adjacency list representation of the graph
        graph = defaultdict(list)  # Graph adjacency list
        in_degrees = [0] * n  # `in_degrees[i]` represents the number of prerequisites for course `i`

        # Step 2: Populate the graph and in-degree array
        for prerequisite, course in prerequisites:
            graph[prerequisite].append(course)  # Add edge `prerequisite -> course`
            in_degrees[course] += 1  # Increment in-degree of `course`
        
        # Step 3: Initialize the queue with courses that have no prerequisites (in-degree = 0)
        queue = deque()
        for i in range(n):
            if in_degrees[i] == 0:  # If a course has no prerequisites, it can be taken immediately
                queue.append(i)
        
        # Step 4: Process courses in topological order
        enrolled_courses = 0  # Track the number of courses that can be completed
        while queue:
            node = queue.popleft()  # Take a course with no prerequisites
            enrolled_courses += 1  # Count this course as completed

            # Reduce the in-degree of dependent courses
            for neighbor in graph[node]:
                in_degrees[neighbor] -= 1  # Reduce prerequisite count

                # If a dependent course now has no prerequisites, add it to the queue
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: If we could process all courses, return True, otherwise return False
        return enrolled_courses == n  # If we enrolled in all `n` courses, there's no cycle
