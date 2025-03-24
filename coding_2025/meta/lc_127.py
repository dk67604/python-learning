'''
https://leetcode.com/problems/word-ladder/description/

✅ Time Complexity: O(N × M × 26) → Simplifies to O(N × M)
Where:

N is the number of words in the wordList

M is the length of each word

🔍 Explanation:
For each word processed in the BFS queue, you:

Loop through each character position in the word → M

Try replacing it with every letter from 'a' to 'z' → 26 letters

For each transformation, you check if it exists in the dictionary (O(1) due to the set)

So per word:
O(M × 26) = O(M) work

In the worst case, you may explore up to all N words from the dictionary, giving:
👉 Total time = O(N × M)

✅ Space Complexity: O(N × M)
Why:

dictionary_set stores up to N words, each of length M → O(N × M)

visited set also stores up to N words → O(N × M)

queue can store up to N words → O(N × M)

No additional complex data structures used

🧠 Summary:
Time: O(N × M)

Space: O(N × M)

Your solution is efficient because it:

Generates neighbors directly (no need to compare word pairs)

Uses BFS with O(1) lookups via a set
'''

from typing import List
from collections import deque

class Solution:
    def ladderLength(self, start: str, end: str, wordList: List[str]) -> int:
        """
        Given a `start` word and an `end` word, and a list of valid words (`wordList`),
        find the shortest transformation sequence from `start` to `end`,
        where:
        - Each transformed word must exist in `wordList`.
        - Only one letter can be changed at a time.
        - Return the length of the shortest transformation sequence. Return 0 if no sequence exists.
        """

        # Step 1: Convert wordList to a set for O(1) lookup time
        dictionary_set = set(wordList)

        # If `end` word is not in the dictionary, transformation is impossible
        if end not in dictionary_set:
            return 0
        
        # If start and end words are the same, the shortest path is just one step
        if start == end:
            return 1

        # Step 2: BFS Setup
        lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"  # Letters for transformation
        queue = deque([start])  # Initialize queue for BFS
        visited = set([start])  # Track visited words to prevent cycles
        dist = 0  # Distance counter (number of transformation steps)

        # Step 3: BFS Traversal
        while queue:
            dist += 1  # Increment transformation step count
            
            # Process all words at the current level before moving to the next
            for _ in range(len(queue)):
                curr_word = queue.popleft()  # Get the current word

                # If we reach the end word, return the total transformation steps
                if curr_word == end:
                    return dist
                
                # Step 4: Generate all possible one-letter transformations
                for i in range(len(curr_word)):
                    for c in lower_case_alphabet:
                        # Generate a new word by replacing one character
                        next_word = curr_word[:i] + c + curr_word[i+1:]

                        # If the new word exists in dictionary and is not visited, add to queue
                        if next_word in dictionary_set and next_word not in visited:
                            queue.append(next_word)
                            visited.add(next_word)  # Mark as visited to avoid reprocessing

        # Step 5: If BFS completes without finding `end`, return 0 (no transformation possible)
        return 0
