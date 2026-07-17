from bisect import bisect_right
from itertools import accumulate

class Solution:
    def gcdValues(self, nums: list[int], queries: list[int]) -> list[int]:
        max_num = max(nums)
        
        count_divisor = [0] * (max_num + 1)
        for num in nums:
            count_divisor[num] += 1
            
        for i in range(1, max_num + 1):
            for j in range(2 * i, max_num + 1, i):
                count_divisor[i] += count_divisor[j]
                
        count_gcd_pair = [0] * (max_num + 1)
        for gcd in range(max_num, 0, -1):
            v = count_divisor[gcd]
            count_gcd_pair[gcd] = v * (v - 1) // 2
            for larger_gcd in range(2 * gcd, max_num + 1, gcd):
                count_gcd_pair[gcd] -= count_gcd_pair[larger_gcd]
                
        prefix_count_gcd_pair = list(accumulate(count_gcd_pair))
        
        return [bisect_right(prefix_count_gcd_pair, q) for q in queries]