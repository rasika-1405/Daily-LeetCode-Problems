class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # null case
        if prices is None:
            return 0
        
        n = len(prices)
        max_profit = 0
        
        for i in range(n-1):
            # valley condition
            if prices[i] > prices[i+1]:
                continue
            profit = prices[i+1] - prices[i]
            max_profit += profit
        return max_profit