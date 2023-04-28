class Solution:
    def longestPalindrome(self, s: str) -> str:
        # null case
        if s is None:
            return s
        
        n = len(s)
        dp = [False for _ in range(n)]
        start, end = 0, 0
        
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and ((i-j<2) or dp[j+1]):
                    dp[j] = True
                    if i-j > end-start:
                        start = j
                        end = i
                else:
                    dp[j] = False
        return s[start:end+1]