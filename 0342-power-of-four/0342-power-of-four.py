class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 :
            return False
        x = log(n) / log(4)
        if x - int(x) == 0:
            return True
        return False
        