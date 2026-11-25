class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base1, mod1 = 1315423911, (1 << 61) - 1
        base2, mod2 = 1000003, 1_000_000_009
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        for i, val in enumerate(nums):
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + val) % mod1
            h2[i + 1] = (h2[i] * base2 + val) % mod2
        def get_hash(l: int, r: int) -> tuple[int, int]:
            x1 = (h1[r] - h1[l] * p1[r - l]) % mod1
            x2 = (h2[r] - h2[l] * p2[r - l]) % mod2
            return (x1, x2)
        def has_unique_of_len(length: int) -> bool:
            counts: dict[tuple[int, int], int] = {}
            for start in range(n - length + 1):
                key = get_hash(start, start + length)
                counts[key] = counts.get(key, 0) + 1
            return any(cnt == 1 for cnt in counts.values())
        lo, hi, ans = 1, n, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
