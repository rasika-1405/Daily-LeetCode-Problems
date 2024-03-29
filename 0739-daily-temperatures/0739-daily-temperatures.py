class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # null case
        if temperatures is None:
            return [0]
        
        n = len(temperatures)
        result = [0 for _ in range(n)]
        
        temp_stk = []
        for i in range(n):
            while temp_stk and temperatures[i]>temperatures[temp_stk[-1]]:
                idx = temp_stk.pop()
                result[idx] = i - idx
            temp_stk.append(i)
        
        return result
                