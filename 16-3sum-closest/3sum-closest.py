class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum =  nums[0] + nums[1] + nums[2]
        min_diff = abs(closest_sum - target)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(sum-target)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum
                if sum == target:
                    return sum
                if sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum