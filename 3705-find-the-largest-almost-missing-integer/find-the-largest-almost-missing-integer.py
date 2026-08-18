class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        cnt = Counter()
        for i in range(len(nums) - k + 1):
            for x in set(nums[i : i + k]):
                cnt[x] += 1

        candidates = [x for x, c in cnt.items() if c == 1]
        return max(candidates) if candidates else -1