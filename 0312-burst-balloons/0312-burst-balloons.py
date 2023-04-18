class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # null case
        if nums is None:
            return 0
        
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for l in range(1, n+1):
            # form all possible arrays with l = 1,2,3,4
            for i in range(n-l+1):
                j = i+l-1 # end index of formed array
                for k in range(i, j+1): # kth balloon bursting at end
                    # k(end) = before + left*curr*right + after
                    left, right = 1, 1
                    if i!=0:
                        left = nums[i-1]
                    if j!=n-1:
                        right = nums[j+1]
                    before, after = 0, 0
                    if k!=i:
                        before = dp[i][k-1]
                    if k!=j:
                        after = dp[k+1][j]
                    dp[i][j] = max(dp[i][j], before + left*nums[k]*right + after)
        
        return dp[0][n-1]