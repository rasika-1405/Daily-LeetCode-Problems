class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Brute force
        m = len(haystack)
        n = len(needle)
        
        # 2 pointers
        i,j = 0,0
        
        while i <= m-n:
            if haystack[i] == needle[j]:
                k = i
                while haystack[k] == needle[j]:
                    k+=1
                    j+=1
                    if j == n:
                        return i
                j = 0
            i+=1
        return -1