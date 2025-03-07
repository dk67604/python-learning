from collections import Counter
import heapq
class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    # Since this is min heap comparator, we can use the same just by changing equalities
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word  # Lexicographically larger word gets lower priority
        return self.freq < other.freq  # Lower frequency has higher priority in min heap


def k_most_frequent_string_min_heap(words: List[str], k: int) -> List[str]:
    freqs = Counter(words)
    min_heap = []
    for word, freq in freqs.items():
        heapq.heappush(min_heap, Pair(word, freq))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    res = [heapq.heappop(min_heap).word for _ in range(k)]
    res.reverse()
    return res