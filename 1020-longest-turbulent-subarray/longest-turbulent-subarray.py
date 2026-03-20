class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def get_sign(i):
                if arr[i-1] < arr[i]: return -1
                if arr[i-1] > arr[i]: return 1
                return 0
        n = len(arr)
        if n < 2:
            return n
        res = 1
        l = 0
        for r in range(1, n):
            sign = get_sign(r)
            if sign == 0:
                l = r
            elif r > 1 and sign == get_sign(r - 1):
                l = r - 1
            res = max(res, r - l + 1)
        return res