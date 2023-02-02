class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # null case
        if coins is None or len(coins) == 0:
            return -1
        
        m = len(coins)
        n = amount
        # dp = matrix of M+1, N+1
        dp = [[0]*(n+1)]*(m+1)
        
        # dp[0][0] = 0
        for j in range(1, len(dp[0])):
            dp[0][j] = amount+1
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # if amount is not equal to the denomination
                if j<coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1+dp[i][j-coins[i-1]])
        result = dp[m][n]
        if result > amount:
            return -1
        return result
    
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # null case
#         if coins is None or len(coins) == 0:
#             return -1
        
#         return self.helper(coins, amount, 0, 0)
    
    
#     def helper(self, coins, amount, index, min_count):
#         # base case - if index goes out of bound or amount goes below 0
#         if index == len(coins) or amount < 0:
#             return -1
            
#         if amount == 0:
#             return min_count
        
#         # logic
#         # case 1 choosing the coin
#         case1 = self.helper(coins, amount - coins[index], index, min_count + 1)
        
#         # case 0 not choosing the coin
#         case0 = self.helper(coins, amount, index+1, min_count)
        
#         if case1 == -1:
#             return case0
#         if case0 == -1:
#             return case1
#         return min(case1, case0)