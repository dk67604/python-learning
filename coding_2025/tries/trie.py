# Define a node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}    # Dictionary to store child nodes for each character
        self.is_word = False  # Flag to indicate the end of a complete word


# Define the Trie (prefix tree) structure
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root node of the Trie

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.
        """
        node = self.root
        for c in word:
            # If the character is not already a child, add it
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]  # Move to the child node
        node.is_word = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        """
        Returns True if the word is in the Trie.
        """
        node = self.root
        for c in word:
            # If a character is missing in the Trie path, word doesn't exist
            if c not in node.children:
                return False
            node = node.children[c]  # Move to the next character node
        return node.is_word  # Return True only if this node marks the end of a word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns True if there is any word in the Trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            # If a character is missing, no word with that prefix exists
            if c not in node.children:
                return False
            node = node.children[c]  # Move to the next character node
        return True  # All prefix characters matched, so return True


# Usage Example:
# obj = Trie()
# obj.insert("apple")
# obj.search("apple")      # Returns True
# obj.search("app")        # Returns False
# obj.startsWith("app")    # Returns True
