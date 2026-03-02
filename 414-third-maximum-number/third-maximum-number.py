class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = sorted(list(set(nums)))
        if len(seen) >= 3:
            return seen[-3]
        return seen[-1]
        

