class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        k = 0
        
        for val in pushed:
            stk.append(val)
            while stk and stk[-1] == popped[k]:
                stk.pop()
                k += 1
        
        return k == len(popped)