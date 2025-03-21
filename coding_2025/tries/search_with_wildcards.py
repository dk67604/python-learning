# Define a node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}    # Dictionary to store child nodes for each character
        self.is_word = False  # Flag to indicate the end of a complete word


# Define the WordDictionary class that supports wildcard search using '.'
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root node of the Trie

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for c in word:
            # If the character is not already a child of the current node, create it
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]  # Move to the child node
        node.is_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the Trie.
        The word can contain the '.' wildcard character, which matches any letter.
        """

        def search_helper(word_index: int, node: TrieNode) -> bool:
            """
            Recursive helper function for searching.
            :param word_index: Current index in the search word
            :param node: Current Trie node we're exploring
            """
            for i in range(word_index, len(word)):
                c = word[i]

                # Case 1: Wildcard character '.'
                if c == '.':
                    # Try all children nodes for wildcard match
                    for child in node.children.values():
                        if search_helper(i + 1, child):  # Continue search from next character
                            return True
                    return False  # No matching path found for wildcard

                # Case 2: Normal character match
                if c not in node.children:
                    return False  # If the character path doesn't exist, return False
                node = node.children[c]  # Move to the next node

            # If we've finished processing all characters, return whether this node ends a word
            return node.is_word

        # Start searching from index 0 and the root node
        return search_helper(0, self.root)
