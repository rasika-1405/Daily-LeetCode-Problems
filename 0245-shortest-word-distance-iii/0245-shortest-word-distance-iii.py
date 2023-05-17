class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # null case
        if wordsDict is None:
            return 0
        
        # using 2 pointers
        i, j = -1, -1
        min_dist = inf
        
        for idx in range(len(wordsDict)):
            if word1 != word2:
                if wordsDict[idx] == word1:
                    i = idx
                if wordsDict[idx] == word2:
                    j = idx
                if i != -1 and j != -1:
                    min_dist = min(min_dist, abs(i-j))
            else:
                if wordsDict[idx] == word1:
                    if i<j:
                        i = idx
                    else:
                        j = idx
                    if i != -1 and j != -1:
                        min_dist = min(min_dist, abs(i-j))
        return min_dist