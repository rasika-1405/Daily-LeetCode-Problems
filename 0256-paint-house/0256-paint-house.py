class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # null case
        if costs is None or len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        for j in range(3):
            dp[n-1][j] = costs[n-1][j]
        
        for i in range(n-2, -1, -1):
            dp[i][0] = costs[i][0] + min(dp[i+1][1], dp[i+1][2])
            dp[i][1] = costs[i][1] + min(dp[i+1][0], dp[i+1][2])
            dp[i][2] = costs[i][2] + min(dp[i+1][0], dp[i+1][1])
        
        return min(dp[0][0], min(dp[0][1], dp[0][2]))
    # exhaustive approach
#     def minCost(self, costs: List[List[int]]) -> int:
#         # null case
#         if costs is None or len(costs) == 0:
#             return 0
        
#         caseR = self.helper(costs, 0, 0, 0)
#         caseB = self.helper(costs, 0, 1, 0)
#         caseG = self.helper(costs, 0, 2, 0)
#         return min(caseR, caseB, caseG)
    
#     def helper(self, costs, index, color, amount):
#         # base case
#         if index == len(costs):
#             return amount
#         # red = 0, blue = 1, green = 1
#         # logic
#         # if color == 0: blue and green case
#         if color == 0:
#             return min(self.helper(costs, index+1, 1, amount + costs[index][0]), self.helper(costs, index+1, 2, amount + costs[index][0]))
        
#         if color == 1:
#             return min(self.helper(costs, index+1, 0, amount + costs[index][1]), self.helper(costs, index+1, 2, amount + costs[index][1]))
        
#         if color == 2:
#             return min(self.helper(costs, index+1, 0, amount + costs[index][2]), self.helper(costs, index+1, 1, amount + costs[index][2]))
#         return 0