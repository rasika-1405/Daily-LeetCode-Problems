class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # edge case
        if n<=0:
            return False
        x = log(n) / log(2)
        print (x)
        if x - int(x) <= 0.000000001:
            return True
        return False