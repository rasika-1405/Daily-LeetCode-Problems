class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # both strings are equal
        if s == p or p == "*":
            return True
        sl = len(s)
        pl = len(p)
        
        # Using DP
#         dp = [[False for _ in range(sl+1)] for _ in range(pl+1)]
#         dp[0][0] = True
        
#         # values in first column
#         for i in range(1, pl+1):
#             if p[i-1] == "*":
#                 dp[i][0] = dp[i-1][0]
        
#         for i in range(1, pl+1):
#             for j in range(1, sl+1):
#                 if p[i-1] != "*":
#                     if p[i-1] == s[j-1] or p[i-1] == "?":
#                         dp[i][j] = dp[i-1][j-1]
#                 else:
#                     # case0 or case1
#                     dp[i][j] = dp[i-1][j] or dp[i][j-1]
        
#         return dp[pl][sl]

        # Using 2 pointers
        s_star = -1
        p_star = -1
        sp, pp = 0, 0
        
        while sp<sl:
            if pp < pl and (s[sp] == p[pp] or p[pp] == "?"):
                sp+=1
                pp+=1
            elif pp < pl and p[pp] == "*":
                s_star = sp
                p_star = pp
                pp += 1
            elif p_star == -1:
                return False
            else:
                sp = s_star + 1
                s_star = sp
                pp = p_star + 1
        
        while pp<pl:
            if p[pp] != "*":
                return False
            pp+=1
        return True
            