class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        char_map = {}
        word_map = {}
        
        word_list = s.split()
        if len(pattern) != len(word_list):
            return False
        
        for i in range(len(pattern)):
            if word_list[i] in char_map:
                if char_map[word_list[i]] != pattern[i]:
                    return False
            else:
                char_map[word_list[i]] = pattern[i]
            
            if pattern[i] in word_map:
                if word_map[pattern[i]] != word_list[i]:
                    return False
            else:
                word_map[pattern[i]] = word_list[i]
        
        return True