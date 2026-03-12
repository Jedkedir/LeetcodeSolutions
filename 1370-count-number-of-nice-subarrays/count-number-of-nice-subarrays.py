class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = {0: 1} 
        curr_sum = 0
        res = 0
        for n in nums:
            curr_sum += n % 2
            if curr_sum - k in count:
                res += count[curr_sum - k]
            count[curr_sum] = count.get(curr_sum, 0) + 1
        return res
        