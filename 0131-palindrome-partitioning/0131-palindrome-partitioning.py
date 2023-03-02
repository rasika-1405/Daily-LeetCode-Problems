class Solution:
    result = []
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        
        #null case
        if s is None:
            return self.result
        
        self.helper(s, 0, [])
        return self.result
        
    def check_palindrome(self, s):
        return s == s[::-1]
    
    def helper(self, s, pivot, path):
        # base case
        if pivot == len(s):
            self.result.append(path.copy())
            return
        # logic
        
        for i in range(pivot, len(s)):
            subs = s[pivot:(i+1)]
            if self.check_palindrome(subs):
                path.append(subs) #action
                self.helper(s, i+1, path) # recurse
                path.pop() # backtrack
    