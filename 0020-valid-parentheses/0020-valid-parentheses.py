class Solution:
    def isValid(self, s: str) -> bool:
        # Using Stack
        stk = []
        
        # Dictionary for matching parenthesis
        paren = {"(" : ")", "{" : "}", "[" : "]"}
        
        for bracket in s:
            if bracket in paren:
                stk.append(bracket)
            else:
                if len(stk) == 0:
                    return False
                open_brkt = stk.pop()
                if bracket != paren[open_brkt]:
                    return False
        return len(stk) == 0