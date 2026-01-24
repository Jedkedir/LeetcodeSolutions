class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        nums.sort()
        for num in range(0,n):
            if num != nums[i]:
                return num
            i += 1
        return n

        