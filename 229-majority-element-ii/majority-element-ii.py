class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = []
        for num,freq in count.items():
            if freq > n//3:
                res.append(num)
        return res