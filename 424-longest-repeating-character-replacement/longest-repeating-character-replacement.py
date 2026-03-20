class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        freq, l, res = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] += 1
            freq = max(freq, count[s[r]])
            if (r - l + 1) - freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
