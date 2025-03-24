'''
https://leetcode.com/problems/word-break-ii/description/

✅ Time Complexity:
Let:

n be the length of the string s

k be the average number of valid words that can start at each position

L be the average length of the result sentences

Time Complexity (Worst Case): O(2^n × L)
Explanation:

At each character position in the string, we can either break or not (depending on word matches), leading to up to 2^n recursive paths (just like generating all subsets).

For each valid path (sentence), joining words into a string takes O(L), where L is the sentence length.

So total time can be up to O(2^n × L).

Note: In practice, we may use memoization (caching results for subproblems) to reduce redundant recomputation, improving performance significantly.

✅ Space Complexity: O(n × L)
Explanation:

The recursion stack can go as deep as n in the worst case.

The result list may contain up to 2^n sentences, and each sentence takes O(L) space.

So the output space (not auxiliary) can also be O(2^n × L), but auxiliary space is mainly from recursion and temporary lists: O(n × L).


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

'''
Time Complexity: Still up to O(2^n × L) in the worst case (if there are many overlapping subproblems and valid paths), but practically much faster due to avoiding repeated work.

Space Complexity: O(n × L) for recursion + memoization cache.
'''

from typing import List

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        Returns all possible sentences by segmenting the string `s` into valid dictionary words.
        Each sentence is a sequence of words separated by spaces.
        """
        word_set = set(wordDict)  # Convert wordDict to a set for fast lookup
        memo = {}  # Dictionary for memoization

        def backtrack(start_index: int) -> List[str]:
            """
            Recursive backtracking function with memoization to build valid word sequences.

            :param start_index: The starting index in `s` to search for the next word
            :return: A list of sentences that can be built from start_index to end of s
            """
            if start_index in memo:
                return memo[start_index]

            if start_index == len(s):
                return [""]  # Base case: return list with empty string to build sentence

            sentences = []

            # Try every possible substring starting from start_index
            for end_index in range(start_index + 1, len(s) + 1):
                word = s[start_index:end_index]
                if word in word_set:
                    rest_sentences = backtrack(end_index)

                    for sentence in rest_sentences:
                        if sentence:
                            sentences.append(word + " " + sentence)
                        else:
                            sentences.append(word)

            memo[start_index] = sentences
            return sentences

        return backtrack(0)
