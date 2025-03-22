'''
https://leetcode.com/problems/word-search-ii/description/
'''

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}      # Maps character to TrieNode
        self.word = None        # Stores the complete word at the terminal node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build the Trie from the list of words
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                # Create a new TrieNode if char not already a child
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word in the Trie

        res = []  # Result list to store words found on the board

        def dfs(r: int, c: int, node: TrieNode):
            """
            Perform DFS from the board cell at (r, c), traversing Trie as we match characters.
            """
            # If this node marks the end of a word, collect it
            if node.word:
                res.append(node.word)
                node.word = None  # Avoid duplicate entries

            temp = board[r][c]
            board[r][c] = '#'  # Mark the current cell as visited

            # Define possible directions: up, left, down, right
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in dirs:
                next_r, next_c = r + dr, c + dc
                # Check bounds and whether next character is part of Trie path
                if (0 <= next_r < len(board) and 
                    0 <= next_c < len(board[0]) and 
                    board[next_r][next_c] in node.children):
                    dfs(next_r, next_c, node.children[board[next_r][next_c]])

            board[r][c] = temp  # Backtrack: unmark the visited cell

        # Step 2: Start DFS from every cell that matches a starting character in Trie
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in root.children:
                    dfs(r, c, root.children[board[r][c]])

        return res
