'''
https://leetcode.com/problems/group-shifted-strings/description/

Sure! Here's the time and space complexity explanation for your groupStrings function:

✅ Time Complexity: O(n × m)
Where:

n is the number of strings in the input list strings

m is the maximum length of any string

Explanation:
For each of the n strings:

The get_hash function iterates through the string (up to m - 1 character pairs) → O(m)

Hash key generation (including string concatenation) takes O(m) in practice because it handles up to m characters.

Adding strings to a dictionary and converting to list(groups.values()) are also O(n) operations in total.

So, the total time is:

text
Copy
Edit
O(n × m) → processing all n strings of length up to m
✅ Space Complexity: O(n × m)
Explanation:

The hash map stores all n strings grouped by their hash key.

In the worst case (no groups share a hash key), each string is stored once → O(n × m) space in total.

Each hash key (as a string) also takes up to O(m) space.


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
