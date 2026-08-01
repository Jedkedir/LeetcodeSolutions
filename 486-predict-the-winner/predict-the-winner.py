class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def get_score(l, r):
            if l == r:
                return nums[l]
            state = (l, r)
            if state in memo:
                return memo[state]
            pick_l = nums[l] - get_score(l + 1, r)
            pick_r = nums[r] - get_score(l, r - 1)
            memo[state] = max(pick_l, pick_r)
            return memo[state]
        return get_score(0, len(nums) - 1) >= 0