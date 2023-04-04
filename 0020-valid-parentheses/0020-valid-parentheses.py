class Solution:
    def isValid(self, s: str) -> bool:
        
        # null case
        if s is None:
            return True
        
        # optimization
        if len(s)%2 != 0:
            return False
        
        stk = []
        
        # Dictionary for matching parenthesis
        paren = {"(" : ")", "{" : "}", "[" : "]"}
        
        for bracket in s:
            if bracket in paren:
                stk.append(paren[bracket])
            else:
                if len(stk) == 0 or bracket != stk.pop():
                    return False
        return len(stk) == 0