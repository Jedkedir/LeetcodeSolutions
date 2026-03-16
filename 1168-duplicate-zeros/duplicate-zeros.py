class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        idx = n + zeros - 1
        for i in range(n - 1, -1, -1):
            if idx < n:
                arr[idx] = arr[i]
            if arr[i] == 0:
                idx -= 1
                if idx < n:
                    arr[idx] = 0
            idx -= 1
        