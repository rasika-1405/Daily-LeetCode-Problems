class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashset = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(dp)):
            for j in range(i):
                if dp[j] and s[j:i] in hashset:
                    dp[i] = True
                    break
        return dp[len(s)]
    
    