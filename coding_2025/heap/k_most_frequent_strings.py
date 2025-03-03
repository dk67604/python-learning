class Pair:
    def __init__(self, str, freq):
        self.str = str
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq