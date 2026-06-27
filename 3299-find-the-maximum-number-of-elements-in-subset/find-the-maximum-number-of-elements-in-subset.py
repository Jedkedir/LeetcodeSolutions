class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        max_subset = 1
        if 1 in count:
            ones = count[1]
            if ones % 2 == 0:
                max_subset = max(max_subset, ones - 1)
            else:
                max_subset = max(max_subset, ones)
        for num in count:
            if num == 1: continue
            curr = num
            curr_len = 0
            while curr in count and count[curr] >= 2:
                curr_len += 2
                curr = curr * curr
            if curr in count and count[curr] >= 1:
                curr_len += 1
            else:
                curr_len -= 1
            max_subset = max(max_subset, curr_len)
        return max_subset