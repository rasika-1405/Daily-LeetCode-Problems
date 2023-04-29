class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # edge case
        if divisor == 0:
            return inf
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        dividend1 = abs(dividend)
        divisor1 = abs(divisor)
        result = 0
        while dividend1 >= divisor1:
            shifts = 0
            while dividend1 >= (divisor1<<shifts):
                shifts+=1
            shifts-=1
            result += 1<<shifts #2^shifts
            dividend1 = dividend1 - (divisor1<<shifts)
        
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return result
        return -result