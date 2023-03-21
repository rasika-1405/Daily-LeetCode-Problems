class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr is None:
            return 0
        
        n = len(arr)
        dp = [0 for _ in range(n)]
        dp[0] = arr[0]
        
        for i in range(1,n):
            max_sum = arr[i]
            for j in range(1,k+1):
                if i-j+1>=0:    
                    max_sum = max(max_sum, arr[i-j+1])
                    curr_partition = max_sum*j
                    if i-j>=0:
                        curr_partition = max_sum*j+dp[i-j]
                    dp[i] = max(dp[i], curr_partition)
        return dp[n-1]