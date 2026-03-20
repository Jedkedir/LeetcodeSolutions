class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        w_size = n - k
        total = sum(cardPoints)
        if w_size == 0:
            return total
        curr = sum(cardPoints[:w_size])
        min_sum = curr
        for i in range(w_size, n):
            curr += cardPoints[i] - cardPoints[i - w_size]
            min_sum = min(min_sum, curr)
        return total - min_sum