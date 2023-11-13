class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n == 0) return 0;
        int maxProfit = 0;
        int peak = prices[0];
        int valley = prices[0];
        int i = 0;
        
        while(i<n-1){
            if((i<n-1) && (prices[i] >= prices[i+1])) i++;
            valley = prices[i];
            if((i<n-1) && (prices[i] <= prices[i+1])) i++;
            peak = prices[i];
            maxProfit += peak-valley;
        }
        return maxProfit;
    }
}