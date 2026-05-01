class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647  
        MIN_INT = -2147483648 
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        is_negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            dividend -= temp_divisor
            quotient += count
        return -quotient if is_negative else quotient