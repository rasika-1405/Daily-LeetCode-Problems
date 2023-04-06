class Solution:
    def candy(self, ratings: List[int]) -> int:
        # null case
        if ratings is None:
            return 0
        
        n = len(ratings)
        candies = [1 for _ in range(n)]
        
        # left pass
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
    
        total = candies[-1]
        
        # right pass
        for i in range(n-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
            total += candies[i]
            
        return total