class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = [p[0] for p in points]
        x.sort()
        max_width = 0
        for i in range(len(x) - 1):
            width = x[i+1] - x[i]
            if width > max_width:
                max_width = width
        return max_width