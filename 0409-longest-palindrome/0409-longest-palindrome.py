class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        temp_set = set()
        for char in s:
            if char in temp_set:
                count += 2
                temp_set.remove(char)
            else:
                temp_set.add(char)
        if len(temp_set) != 0:
            count += 1
        return count
        