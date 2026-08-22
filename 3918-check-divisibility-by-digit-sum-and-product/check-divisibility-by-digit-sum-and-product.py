class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        digit_sum = sum(digits)
        digit_prod = math.prod(digits)
        divisor = digit_sum + digit_prod
        return divisor != 0 and n % divisor == 0