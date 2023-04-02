class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # null case
        if num is None:
            return ""
        
        if len(num) <= k:
            return "0"
        
        stk = []
        
        # iterating over the string
        for char in num:
            while k and stk and stk[-1] > char:
                stk.pop()
                k-=1
            stk.append(char)
            
        # stack is not empty
        if k:
            result = stk[:-k]
        else:
            result = stk
            
        return str(int("".join(result)))
            