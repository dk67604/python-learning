'''
https://leetcode.com/problems/word-break-ii/description/
'''
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Returns all possible sentences by segmenting the string `s` into valid dictionary words.
        Each sentence is a sequence of words separated by spaces.
        """

        word_set = set(wordDict)  # Convert wordDict to a set for fast lookup
        result = []  # List to store all valid sentences

        def backtrack(s: str, current_sentence: List[str], start_index: int):
            """
            Recursive backtracking function to build valid word sequences.
            
            :param s: The input string
            :param current_sentence: List of words forming the current sentence
            :param start_index: The starting index in `s` to search for the next word
            """
            # Base case: if we've reached the end of the string, store the complete sentence
            if start_index == len(s):
                result.append(" ".join(current_sentence))  # Join the words with spaces
                return

            # Try every possible substring starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]  # Current substring to test
                if word in word_set:
                    current_sentence.append(word)               # Choose the word
                    backtrack(s, current_sentence, end_index)   # Recurse with updated index
                    current_sentence.pop()                      # Backtrack: remove the last word

        # Start backtracking from index 0 with an empty sentence
        backtrack(s, [], 0)
        return result
