class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        # null case
        if s is None:
            return result
        
        char_map = {}
        
        for i in range(len(s)):
            char = s[i]
            char_map[char] = i
        
        start, end = 0,0
        
        for i in range(len(s)):
            char = s[i]
            end = max(end, char_map[char])
            if i == end:
                result.append(end-start+1)
                start = i+1
            
        return result
        