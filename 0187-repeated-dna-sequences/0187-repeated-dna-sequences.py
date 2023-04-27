class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Using sliding window
#         result = set()
#         substr = set()
        
#         for i in range(len(s)-10+1):
#             sub = s[i:i+10]
#             if sub in substr:
#                 result.add(sub)
#             else:
#                 substr.add(sub)
                
#         return list(result)

        # Using Robin Karp
        if len(s) < 10:
            return []
        seen = set()
        result = set()
        
        hash_map = {"A":1, "C":2, "G":3, "T":4}
        hash_code = 0
        
        for i in range(10):
            char = s[i]
            hash_code = hash_code*4 + hash_map[char]
        seen.add(hash_code)
        for i in range(10, len(s)):
            # incoming character
            in_char = s[i]
            hash_code = hash_code*4 + hash_map[in_char]
            # outgoing character
            out_char = s[i-10]
            hash_code = hash_code - hash_map[out_char]*int(pow(4, 10))
            if hash_code in seen:
                result.add(s[i-9:i+1])
            else:
                seen.add(hash_code)
        
        return list(result)