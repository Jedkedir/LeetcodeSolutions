class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        curr = 0
        max_ = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                curr -= nums[l]
                l += 1
            seen.add(nums[r])
            curr += nums[r]
            if curr > max_:
                max_ = curr
        return max_