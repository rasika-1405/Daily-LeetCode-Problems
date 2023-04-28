class Solution:
    def longestPalindrome(self, s: str) -> str:
        # null case
        if s is None:
            return s
        
        # Using DP
#         n = len(s)
#         dp = [False for _ in range(n)]
#         start, end = 0, 0
        
#         for i in range(n):
#             for j in range(i+1):
#                 if s[i] == s[j] and ((i-j<2) or dp[j+1]):
#                     dp[j] = True
#                     if i-j > end-start:
#                         start = j
#                         end = i
#                 else:
#                     dp[j] = False
#         return s[start:end+1]
    
        # Using Extend around center
        n = len(s)
        start, end = 0, 0
        
        def extend_around_center(left, right):
            nonlocal start, end
            while left>= 0 and right <=len(s) - 1 and s[left] == s[right]:
                left-=1
                right+=1
            left+=1
            right-=1
            if right-left > end-start:
                end = right
                start = left
            
        for i in range(n):
            extend_around_center(i, i) # odd case
            if i<n-1:
                extend_around_center(i, i+1) # even case
            
        return s[start:end+1]