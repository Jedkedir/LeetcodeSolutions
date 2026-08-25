class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        seen = set(nums)
        ans = k
        while ans in seen:
            ans += k
        return ans