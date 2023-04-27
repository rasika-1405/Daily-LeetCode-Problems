class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        substr = set()
        
        for i in range(len(s)-10+1):
            sub = s[i:i+10]
            if sub in substr:
                result.add(sub)
            else:
                substr.add(sub)
                
        return list(result)