class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pali(l + 1, r) or is_pali(l, r - 1)
            l += 1
            r -= 1
        return True