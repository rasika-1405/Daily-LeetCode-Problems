class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # null case
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        max_len = 0
        
        # Using Hashmap
#         char_map = {}
#         slow = 0
        
#         for fast in range(len(s)):
#             char = s[fast]
#             if char in char_map:
#                 slow = max(slow, char_map[char]+1)
#             max_len = max(max_len, fast-slow+1)
#             char_map[char] = fast

        # Using Hashsets
        char_set = set()
        char_set.add(s[0])
        slow, fast = 0, 1
        
        while fast < len(s):
            char = s[fast]
            if char in char_set:
                while s[slow] != char:
                    char_set.remove(s[slow])
                    slow += 1
                slow += 1
            max_len = max(max_len, fast-slow+1)
            char_set.add(char)
            fast += 1
        
        return max_len
        