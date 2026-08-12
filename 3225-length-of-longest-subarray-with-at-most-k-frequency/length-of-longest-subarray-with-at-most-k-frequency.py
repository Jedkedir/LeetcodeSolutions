class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        counts = Counter()
        left = 0
        ans = 0

        for right, num in enumerate(nums):
            counts[num] += 1
            while counts[num] > k:
                counts[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans