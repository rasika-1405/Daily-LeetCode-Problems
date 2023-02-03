class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # null case
        if coins is None or len(coins) == 0:
            return 0
        m = len(coins)
        n = amount
        dp = [[0]*(n+1)]*(m+1)
        dp[0][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(0, len(dp[0])):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
        return dp[m][n]
    
    # exhaustive approach
#     def change(self, amount: int, coins: List[int]) -> int:
#         # null case
#         if coins is None or len(coins) == 0:
#             return 0
#         return self.helper(coins, amount, 0)
    
#     def helper(self, coins, amount, index):
#         # base case
#         if amount == 0:
#             return 1
#         if amount < 0 or index == len(coins):
#             return 0
        
#         #logic
#         # choosing the coin
#         case1 = self.helper(coins, amount - coins[index], index)
#         # not choosing the coin
#         case0 = self.helper(coins, amount, index+1)
        
#         return case1+case0