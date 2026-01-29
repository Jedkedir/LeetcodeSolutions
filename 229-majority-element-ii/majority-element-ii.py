class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = []
        for num in set(nums):
            if count[num] > n//3:
                res.append(num)
        return res