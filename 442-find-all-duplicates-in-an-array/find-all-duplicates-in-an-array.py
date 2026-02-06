class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_set = set()
        duplicates = []
        for num in nums:
            if num in num_set:
                duplicates.append(num)
            else:
                num_set.add(num)
        return duplicates