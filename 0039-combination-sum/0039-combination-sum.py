class Solution:
    result = []
    # brute force
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         self.result = []
        
#         # null case
#         if candidates is None:
#             return self.result
        
#         self.helper(candidates, 0, target, [])
#         return self.result
        
#     def helper(self, candidates, i, amount, path):
#         # base case
#         if amount < 0 or i == len(candidates):
#             return
#         if amount == 0:
#             temp = path.copy()
#             self.result.append(temp)
#             return
        
#         # logic
#         # not choose
#         self.helper(candidates, i+1, amount, path)
#         # choose
#         path.append(candidates[i]) # action
#         self.helper(candidates, i, amount-candidates[i], path) # recurse
#         path.pop() # backtrack

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        
        # null case
        if candidates is None:
            return self.result
        
        self.helper(candidates, 0, target, [])
        return self.result
    
    def helper(self, candidates, pivot, amount, path):
        # base case
        if amount < 0:
            return
        if amount == 0:
            self.result.append(path)
            return
        
        # logic
        for i in range(pivot, len(candidates)):
            temp = path.copy()
            temp.append(candidates[i])
            self.helper(candidates, i, amount-candidates[i], temp)
        
        
        
        
        