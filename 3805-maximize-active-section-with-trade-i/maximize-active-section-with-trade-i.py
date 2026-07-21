class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        total_ones = s.count('1')
        zeros = [len(b) for b in s.split('1') if b]
        if len(zeros) < 2:
            return total_ones
        max_gain = max(zeros[i] + zeros[i + 1] for i in range(len(zeros) - 1))
        return total_ones + max_gain