class Solution:
    def reverseBits(self, n: int) -> int:
        # print(n)
        out = bin(n)
        out = "".join(['0' for _ in range(32-len(out)+2)]) + str(out[2:])
        
        signed_number = 0
        for i in range(len(out)):
            if out[i] == "0":
                continue
            signed_number += pow(2, i)
        
        return signed_number