class Solution:
    def countGoodNumbers(self, n: int) -> int:
        even_pos = (n + 1) // 2
        odd_pos = n // 2
        modulo = 10**9 + 7
        first_part = pow(5, even_pos, modulo)
        second_part = pow(4, odd_pos, modulo)
        return (first_part * second_part) % modulo