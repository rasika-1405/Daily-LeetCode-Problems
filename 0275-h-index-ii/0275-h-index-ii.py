class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # null case
        if citations is None:
            return 0
        
        n = len(citations)
        
        # linear search
        # for i in range(n):
        #     diff = n - i
        #     if diff<=citations[i]: # h-index
        #         return diff
        # return 0
        
        # binary search
        low = 0
        high = n-1
        
        while low<= high:
            mid = low + (high-low) // 2
            diff = n-mid
            if citations[mid] == diff:
                return diff
            elif citations[mid] < diff:
                low=mid+1
            else:
                high=mid-1
        return n-low
