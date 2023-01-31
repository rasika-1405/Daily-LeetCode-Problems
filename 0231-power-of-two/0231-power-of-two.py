class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # # approach -1
        # # edge case
        # if n<=0:
        #     return False
        # x = log(n) / log(2)
        # if x - int(x) <= 0.000000001:
        #     return True
        # return False
        
        # approach - 2
        if n<=0:
            return False
        
        binary_value = str(bin(n))[2:]
        count = 0
        for i in range(len(binary_value)):
            if binary_value[i] == '1':
                count += 1
            if count > 1:
                return False
        return True