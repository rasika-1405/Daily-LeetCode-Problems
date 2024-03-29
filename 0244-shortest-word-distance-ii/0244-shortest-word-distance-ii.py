class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.word_map = defaultdict(list)
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            self.word_map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        li1 = self.word_map[word1]
        li2 = self.word_map[word2]
        result = inf
        p1, p2 = 0, 0
        
        while p1<len(li1) and p2<len(li2):
            idx1 = li1[p1]
            idx2 = li2[p2]
            result = min(result, abs(idx1-idx2))
            if idx1<idx2:
                p1+=1
            else:
                p2+=1
        return result


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)