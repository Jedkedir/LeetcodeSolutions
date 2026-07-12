class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {val: idx + 1 for idx, val in enumerate(sorted(set(arr)))}
        return [ranks[num] for num in arr]