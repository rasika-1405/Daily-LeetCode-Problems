class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_map = {}
        
        # creating freq map
        for char in s:
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1
        
        result = ""
        
        # adding characters from the order string
        for char in order:
            if char in char_map:
                count = char_map[char]
                for k in range(count):
                    result += char
                char_map.pop(char)
        
        # adding remaining characters
        for key in char_map:
            count = char_map[key]
            for k in range(count):
                result += key
        
        return result