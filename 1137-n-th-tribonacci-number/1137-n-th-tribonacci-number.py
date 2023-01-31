class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        p = 0
        q = 1
        r = 1
        
        for i in range(3,n+1):
            f_n = p + q + r
            p = q
            q = r
            r = f_n
        return f_n
            