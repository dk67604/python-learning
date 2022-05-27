"""
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int val) Adds the integer val to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi].


Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
"""
import heapq
from typing import List

class SummaryRanges:

        def __init__(self):
            self.intervals = []
            self.seen = set()
    
        def addNum(self, val: int) -> None:
            if val not in self.seen:
                self.seen.add(val)
                heapq.heappush(self.intervals, [val, val])
    
        def getIntervals(self) -> List[List[int]]:
            tmp = []
            while self.intervals:
                cur = heapq.heappop(self.intervals)
                if tmp and cur[0] <= tmp[-1][1] + 1:
                    tmp[-1][1] = max(tmp[-1][1], cur[1])
                else:
                    tmp.append(cur)
            self.intervals = tmp
            return self.intervals


if __name__ == '__main__':
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)
    print(summaryRanges.getIntervals())
