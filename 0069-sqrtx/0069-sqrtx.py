class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        #using binary search
        min = 0
        max = x
        mid = (min+max)//2
        
        while min<max:
            temp = mid * mid
            if temp == x:
                return mid
            elif temp < x:
                min = mid + 1
            else:
                max = mid
            mid = (min+max) // 2
        return mid - 1