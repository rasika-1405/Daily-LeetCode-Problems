class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # null case
        if citations is None:
            return 0
        
        n = len(citations)
        # Brute force
#         citations = sorted(citations)
        
#         # linear search
#         for i in range(n):
#             diff = n - i
#             if diff<=citations[i]: # h-index
#                 return diff
#         return 0
        
        # using count sort
        buckets = [0 for _ in range(n+1)]
        
        for i in range(n):
            if citations[i] >= n:
                buckets[n] += 1
            else:
                buckets[citations[i]]+=1
        sum=0
        # iterate in reversed order
        for i in range(n, -1, -1):
            sum += buckets[i]
            if sum >= i:
                return i
        return 0