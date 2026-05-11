class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            temp = []
            while num > 0:
                temp.append(num % 10)
                num //= 10
            res.extend(reversed(temp))
        return res