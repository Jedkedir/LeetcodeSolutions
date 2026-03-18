class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        chars = Counter(s)
        a = ["Q","W","E","R"]
        if all(chars[char] <= (n//4)for char in a):
            return 0
        l = 0
        res = n
        for r in range(n):
            chars[s[r]] -= 1
            while l < n and all(chars[char] <= (n//4) for char in a):
                res = min(res, r - l + 1)
                chars[s[l]] += 1
                l += 1
        return res
        

