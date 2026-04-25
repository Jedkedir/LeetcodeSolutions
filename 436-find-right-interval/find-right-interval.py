class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_starts = sorted([[interval[0], i] for i, interval in enumerate(intervals)])
        starts_only = [item[0] for item in sorted_starts]
        res = []
        for interval in intervals:
            end = interval[1]
            i = bisect.bisect_left(starts_only, end)
            if i < len(intervals):
                res.append(sorted_starts[i][1])
            else:
                res.append(-1)
        return res