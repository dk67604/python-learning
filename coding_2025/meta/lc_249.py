'''
https://leetcode.com/problems/group-shifted-strings/description/
'''
from collections import defaultdict
from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        # Function to generate a unique hash key for each shift group
        def get_hash(string: str):
            key = []
            
            # Iterate through the string to calculate shift differences
            for i in range(1, len(string)):
                diff = ord(string[i]) - ord(string[i-1])  # Calculate difference between adjacent characters
                
                # If difference is negative, adjust for circular shift in alphabet
                if diff < 0:
                    diff += 26
                
                # Store the difference with a separator to create a unique pattern
                key.append(str(diff) + '#')
            
            # Append a special character to distinguish different shift groups
            key.append('.')
            
            # Return the generated hash key as a string
            return ''.join(key)

        # Dictionary to group strings by their computed hash keys
        groups = defaultdict(list)
        
        # Iterate over all strings in the input list
        for string in strings:
            hash_key = get_hash(string)  # Compute the unique shift-based hash
            groups[hash_key].append(string)  # Group the strings based on their hash
        
        # Return all the grouped values as a list of lists
        return list(groups.values())
