class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sort = sorted(nums)
        for num in nums:
            res.append(sort.index(num))
        return res