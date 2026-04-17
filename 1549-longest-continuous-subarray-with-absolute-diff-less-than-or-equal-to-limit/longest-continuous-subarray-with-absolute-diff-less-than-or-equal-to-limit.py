class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq = deque() 
        min_dq = deque() 
        l = 0
        res = 0
        for r in range(len(nums)):
            while max_dq and nums[r] > max_dq[-1]:
                max_dq.pop()
            max_dq.append(nums[r])
            while min_dq and nums[r] < min_dq[-1]:
                min_dq.pop()
            min_dq.append(nums[r])
            while max_dq[0] - min_dq[0] > limit:
                if nums[l] == max_dq[0]:
                    max_dq.popleft()
                if nums[l] == min_dq[0]:
                    min_dq.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res