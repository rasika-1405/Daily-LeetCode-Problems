class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        freq_map = {}
        
        for char in s:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1
                
        for char in t:
            if char in freq_map:
                freq_map[char] -= 1
                if freq_map[char] == 0:
                    freq_map.pop(char)
        
        return len(freq_map) == 0