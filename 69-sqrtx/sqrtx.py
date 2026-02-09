class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x 
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                l = mid + 1
            else:
                r = mid - 1
        return r 