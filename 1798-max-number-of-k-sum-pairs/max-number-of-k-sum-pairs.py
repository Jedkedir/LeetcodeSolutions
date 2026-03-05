class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter()
        oper = 0
        for num in nums:
            complement = k - num
            if counts[complement] > 0:
                oper += 1
                counts[complement] -= 1 
            else:
                counts[num] += 1
        return oper