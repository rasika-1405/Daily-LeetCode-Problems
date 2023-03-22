class Solution:
    # memo = []
    def uniquePaths(self, m: int, n: int) -> int:
        # null case
        if m == 0 or n == 0:
            return 0
        
        # brute force
        # def dfs(i,j,m,n):
        #     # base case
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i<0 or j<0 or i == m or j == n:
        #         return 0
        #     #logic
        #     return dfs(i,j+1,m,n) + dfs(i+1,j,m,n)
        # return dfs(0,0,m,n)
        
        # Top-down DP
        memo = [[0 for _ in range(n)] for _ in range(m)]
        def dfs_memo(i,j,m,n):
            # base case
            if i == m-1 and j == n-1:
                return 1
            if i<0 or j<0 or i == m or j == n:
                return 0
            #logic
            if memo[i][j] == 0:
                memo[i][j] = dfs_memo(i,j+1,m,n) + dfs_memo(i+1,j,m,n)
            return memo[i][j]
        return dfs_memo(0,0,m,n)
        
        # Bottom-up DP
        # dp = [[0]*(n+1)]*(m+1)
        # dp[m-1][n-1] = 1
        # for i in range(m-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if i == m-1 and j == n-1:
        #             continue
        #         dp[i][j] = dp[i+1][j] + dp[i][j+1]
        # return dp[0][0]
    