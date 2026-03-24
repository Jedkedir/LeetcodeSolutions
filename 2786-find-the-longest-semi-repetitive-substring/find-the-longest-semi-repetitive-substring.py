class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n
        l = 0
        freq = 0
        max_ = 1
        for r in range(1, n):
            if s[r] == s[r-1]:
                freq += 1
            while freq > 1:
                if s[l] == s[l+1]:
                    freq -= 1
                l += 1
            max_ = max(max_, r - l + 1)
        return max_