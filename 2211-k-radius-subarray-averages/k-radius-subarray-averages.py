class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        w_size = 2 * k + 1
        res = [-1] * n
        if w_size > n:
            return res
        curr = sum(nums[:w_size])
        res[k] = curr // w_size
        for i in range(k + 1, n - k):
            curr += nums[i + k] - nums[i - k - 1]
            res[i] = curr // w_size
        return res