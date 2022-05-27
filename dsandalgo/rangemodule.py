import bisect

"""
  What does it mean if i is odd ? If i is odd, that means that preceding element is an even element and the opening 
  of the range is part of some other range. Similarly if j is odd, that also means if it is part of some other range 
  and we need not create a new entry for it.Next, what does it mean if i ie even ? This means that this point is not 
  covered by any existing range and we have to create a new entry for it. Similar thing holds true for j (for j it 
  would mean that we would have overwrite an exiting range).
  https://leetcode.com/problems/range-module/discuss/169353/Ultra-concise-Python-(only-6-lines-of-actual-code)-(also-236ms-beats-100)
"""
class RangeModule:

    def __init__(self):
        self.track = []

    def addRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)

        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)

        self.track[start:end] = subtrack

    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)

        return start == end and start % 2 == 1


if __name__ == '__main__':
    range_module: RangeModule = RangeModule()
    range_module.addRange(left=10, right=20)
    print(range_module.track)
    range_module.removeRange(left=14, right=16)
    print(range_module.track)
    print(range_module.queryRange(10, 14))
    print(range_module.queryRange(13, 15))
