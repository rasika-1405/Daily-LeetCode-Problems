class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        p = 0
        q = 1
        
        for i in range(2,n+1):
            f_n = p + q
            p = q
            q = f_n
        return f_n