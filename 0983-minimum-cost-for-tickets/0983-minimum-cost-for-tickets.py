class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    
#         def helper(i, days, costs, count):
#             # base case
#             if i == len(days):
#                 return count
            
#             # logic
#             case1 = helper(i+1, days, costs, count+costs[0])
#             currday = days[i]
#             j = i
#             while j<len(days) and currday+7 > days[j]:
#                 j+=1
#             case7 = helper(j, days, costs, count+costs[1])
#             j = i
#             while j<len(days) and currday+30 > days[j]:
#                 j+=1
#             case30 = helper(j, days, costs, count+costs[2])
#             return min(case1, case7, case30)
            
        
#         return helper(0, days, costs, 0)

        dp = [inf for _ in range(days[-1]+1)]
        dp[0] = 0
        
        for i in range(1, days[-1]+1):
            if i in days:
                if i-1>=0 and i-7>=0 and i-30>=0:
                    dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
                elif i-1>=0 and i-7>=0:
                    dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[0]+costs[2])
                elif i-1>=0:
                    dp[i] = min(dp[i-1]+costs[0], dp[0]+costs[1], dp[0]+costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]   