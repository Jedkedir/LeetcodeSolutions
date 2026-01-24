class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        while n >= 0:
            if n != nums[n-1]:
                return n
            else:
                n-=1

        