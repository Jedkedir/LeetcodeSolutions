class Solution:
    def uniqueXorTriplets(self, nums: list[int]) -> int:
        n = len(nums)
        mx = max(nums)
        T = 1
        while T <= mx:
            T <<= 1
            
        s1 = [False] * T
        for i in range(n):
            for j in range(i, n):
                s1[nums[i] ^ nums[j]] = True
                
        s2 = [False] * T
        for i in range(T):
            if s1[i]:
                for num in nums:
                    s2[i ^ num] = True
                    
        return sum(s2)