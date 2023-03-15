class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def cal_lps(needle):
            lps = [0 for _ in range(len(needle))]
            i, j = 1,0
            while i<len(needle):
                if needle[j] == needle[i]:
                    j+=1
                    lps[i] = j
                    i+=1
                elif needle[j] != needle[i] and j>0:
                    j = lps[j-1]
                elif needle[j] != needle[i] and j==0:
                    lps[i] = 0
                    i+=1
            return lps
        
        m = len(haystack)
        n = len(needle)
        
        # 2 pointers
        i,j = 0,0
        
        # Brute force
        # while i <= m-n:
        #     if haystack[i] == needle[j]:
        #         k = i
        #         while haystack[k] == needle[j]:
        #             k+=1
        #             j+=1
        #             if j == n:
        #                 return i
        #         j = 0
        #     i+=1
        # return -1
        
        # Using KMP algorithm
        if m<n:
            return -1
        
        # Using KMP
        lps = cal_lps(needle)
        
        while i<m:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j==n:
                    return i-n
            elif haystack[i] != needle[j] and j>0:
                j = lps[j-1]
            elif haystack[i] != needle[j] and j==0:
                i+=1
        return -1

        # Using Robin Karp
#         k = 26
#         k1 = pow(k, n)
#         needle_hash = 0
        
#         for i in range(len(needle)):
#             char = needle[i]
#             needle_hash = needle_hash * k + (ord(char) - ord('a'))
            
#         # making a window of length needle on haystack
#         haystack_hash = 0
#         for i in range(n):
#             char = haystack[i]
#             haystack_hash = haystack_hash * k + (ord(char) - ord('a'))
#         if haystack_hash == needle_hash:
#             return 0
        
#         # slide the window
#         for i in range(1, m-n+1):
#             in_char = haystack[i+n-1]
#             haystack_hash = haystack_hash * k + (ord(in_char) - ord('a'))
            
#             out_char = haystack[i-1]
#             haystack_hash = haystack_hash - k1 * (ord(out_char) - ord('a'))
            
#             if haystack_hash == needle_hash:
#                 return i
#         return -1