class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # null case
        if len(s) == 0:
            return 0
        
        char_map = {}
        slow = 0
        max_len = 0
        
        for fast in range(len(s)):
            char = s[fast]
            if char in char_map:
                slow = max(slow, char_map[char]+1)
            max_len = max(max_len, fast-slow+1)
            char_map[char] = fast
        return max_len
        