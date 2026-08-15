class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0

        for right, ch in enumerate(s):
            count[ch] += 1
            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans