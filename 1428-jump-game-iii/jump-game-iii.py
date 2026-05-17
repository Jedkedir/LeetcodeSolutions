class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start < 0 or start >= len(arr) or arr[start] < 0:
            return False
        if arr[start] == 0:
            return True
        arr[start] = -arr[start]
        jump_distance = abs(arr[start])
        return self.canReach(arr, start + jump_distance) or self.canReach(arr, start - jump_distance)