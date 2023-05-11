class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # null case
        if prices is None or len(prices)<2:
            return 0
        n = len(prices)
        buy = [0 for _ in range(n)]
        sell = [0 for _ in range(n)]
        buy[0] = -prices[0]
        sell[0] = 0
        buy[1] = max(buy[0], 0 - prices[1])
        sell[1] = max(0, buy[0] + prices[1])
        
        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])
        
        return max(buy[n-1], sell[n-1])