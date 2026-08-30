class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        both_left = j + 1
        both_right = n - i
        one_each = (i + 1) + (n - j)
        return min(both_left, both_right, one_each)