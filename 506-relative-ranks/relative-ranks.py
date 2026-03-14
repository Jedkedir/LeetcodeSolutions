class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        index = sorted(range(n), key=lambda i: score[i], reverse=True)
        result = [""] * n
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for rank, i in enumerate(index):
            result[i] = medals[rank] if rank < 3 else str(rank + 1)
        return result
