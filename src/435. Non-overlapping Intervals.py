from typing import List
from numpy import inf

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        ans = 0
        k = -inf
        for x, y in intervals:
            if x < k:
                ans += 1
            else:
                k = y
        return ans



intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

sol = Solution()
sol.eraseOverlapIntervals(intervals)
