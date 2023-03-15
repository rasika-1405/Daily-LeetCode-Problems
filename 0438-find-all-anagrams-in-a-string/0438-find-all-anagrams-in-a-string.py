class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        
        freq_map = {}
        for char in p:
            if char not in freq_map:
                freq_map[char] = 1
            else:
                freq_map[char] += 1
        
        match = 0
        
        for i in range(len(s)):
            # for incoming character
            in_char = s[i]
            if in_char in freq_map:
                count = freq_map[in_char]
                count -= 1
                freq_map[in_char] = count
                if count == 0:
                    match += 1
            
            # for outgoing character
            if i>= len(p):
                out_char = s[i-len(p)]
                if out_char in freq_map:
                    count = freq_map[out_char]
                    count += 1
                    freq_map[out_char] = count
                    if count == 1:
                        match -= 1
            
            if match == len(freq_map):
                result.append(i-len(p)+1)
                
        return result
            