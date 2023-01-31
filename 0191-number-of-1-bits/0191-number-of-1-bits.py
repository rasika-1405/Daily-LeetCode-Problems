class Solution:
    def hammingWeight(self, n: int) -> int:
        out = str(bin(n))[2:]
        count = 0
        for i in range(len(out)):
            if out[i] == '1':
                count += 1
        return count