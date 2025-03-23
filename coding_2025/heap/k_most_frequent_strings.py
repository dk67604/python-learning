from collections import Counter
import heapq
from typing import List

# Custom Pair class to store word-frequency pairs in the heap
class Pair:
    def __init__(self, word, freq):
        self.word = word      # the word itself
        self.freq = freq      # its frequency

    # Define comparison logic for the min-heap
    def __lt__(self, other):
        # If frequencies are equal, compare lexicographically (higher comes first, so we reverse it)
        if self.freq == other.freq:
            return self.word > other.word  # Invert comparison to get lexicographically smaller at the top
        return self.freq < other.freq      # Lower frequency = higher priority in min heap


def k_most_frequent_string_min_heap(words: List[str], k: int) -> List[str]:
    """
    Finds the k most frequent words in a list.
    If frequencies match, returns them in lexicographically smaller order.
    Uses a min-heap to efficiently maintain the top k frequent elements.

    :param words: List of words
    :param k: Number of top frequent words to return
    :return: List of top k words, sorted by frequency and lexicographical order
    """

    # Step 1: Count frequencies of each word using Counter
    freqs = Counter(words)

    # Step 2: Initialize a min-heap to keep top k frequent words
    min_heap = []

    # Step 3: Push Pair(word, freq) into the heap
    for word, freq in freqs.items():
        heapq.heappush(min_heap, Pair(word, freq))

        # If heap grows beyond size k, remove the least frequent/lowest priority element
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Step 4: Extract the top k elements from heap into result list
    # They will be in reverse order (smallest freq to largest), so we reverse at the end
    res = [heapq.heappop(min_heap).word for _ in range(k)]
    res.reverse()
    return res
