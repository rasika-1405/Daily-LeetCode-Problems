class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # null case
        if citations is None:
            return 0
        
        n = len(citations)
        citations = sorted(citations)
        
        # linear search
        for i in range(n):
            diff = n - i
            if diff<=citations[i]: # h-index
                return diff
        return 0