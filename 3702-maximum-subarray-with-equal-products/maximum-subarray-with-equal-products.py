class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0
        from math import gcd, lcm
        max_product_bound = lcm(*nums) * max(nums)
        for i in range(n):
            current_product = 1
            current_gcd = 0  
            current_lcm = 1
            for j in range(i, n):
                current_product *= nums[j]
                current_gcd = gcd(current_gcd, nums[j])
                current_lcm = lcm(current_lcm, nums[j])
                if current_product == current_gcd * current_lcm:
                    max_length = max(max_length, j - i + 1)
                if current_product > max_product_bound:
                    break
        return max_length
