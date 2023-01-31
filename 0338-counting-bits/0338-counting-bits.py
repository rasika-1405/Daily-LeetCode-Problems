class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for i in range(n+1):
            binary_value = str(bin(i))[2:]
            count = 0
            for digit in binary_value:
                if digit == '1':
                    count += 1
            ans.append(count)
        return ans