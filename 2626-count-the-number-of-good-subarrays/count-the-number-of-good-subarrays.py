class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = Counter()
        res, pairs, l = 0,0,0
        for r in range(n):
            pairs += count[nums[r]]
            count[nums[r]] += 1
            while pairs >= k:
                res += (n - r)
                count[nums[l]] -= 1
                pairs -= count[nums[l]]
                l += 1
        return res