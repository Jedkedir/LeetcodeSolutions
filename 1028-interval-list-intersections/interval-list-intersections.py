class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        res = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            start = max(firstList[ptr1][0], secondList[ptr2][0])
            end = min(firstList[ptr1][1], secondList[ptr2][1])
            if start <= end:
                res.append([start, end])
            if firstList[ptr1][1] < secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr2 += 1
        return res