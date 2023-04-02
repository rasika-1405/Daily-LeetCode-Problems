class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # null case
        if prices is None:
            return 0
        
        n = len(prices)
        max_profit = 0
        
        # for i in range(n-1):
        #     # valley condition
        #     if prices[i] > prices[i+1]:
        #         continue
        #     profit = prices[i+1] - prices[i]
        #     max_profit += profit
        # return max_profit
        
        peak = prices[0]
        valley = prices[0]
        i=0
        
        while i<n-1:
            # valley condition
            if i<n-1 and prices[i] >= prices[i+1]:
                i+=1
            valley = prices[i]
            if i<n-1 and prices[i] <= prices[i+1]:
                i+=1
            peak = prices[i]
            max_profit += peak - valley
        return max_profit
            