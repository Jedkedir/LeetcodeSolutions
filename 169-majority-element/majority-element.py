class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        maxNum = count.most_common(1)[0]
        return maxNum[0]