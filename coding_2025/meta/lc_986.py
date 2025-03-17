'''
https://leetcode.com/problems/interval-list-intersections/description/?envType=company&envId=facebook&favoriteSlug=facebook-thirty-days
'''
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Finds the intersection of two lists of intervals.
        
        :param firstList: List of intervals [[start1, end1], [start2, end2], ...]
        :param secondList: List of intervals [[startA, endA], [startB, endB], ...]
        :return: A list of intervals representing the intersection of both input lists.
        """
        
        # If either list is empty, return an empty list (no intersection possible)
        if not firstList or not secondList:
            return []
        
        i, j = 0, 0  # Pointers for firstList and secondList
        result = []  # Stores the intersection intervals

        # Traverse both lists until one of them is fully processed
        while i < len(firstList) and j < len(secondList):
            # Calculate the overlapping interval
            startMax = max(firstList[i][0], secondList[j][0])  # Start of the intersection
            endMin = min(firstList[i][1], secondList[j][1])  # End of the intersection
            
            # If the interval is valid (start <= end), add it to the result
            if endMin >= startMax:
                result.append([startMax, endMin])
            
            # Move the pointer for the interval that ends first (to find new intersections)
            if firstList[i][1] == endMin:
                i += 1
            if secondList[j][1] == endMin:
                j += 1
        
        return result  # Return the list of intersected intervals
