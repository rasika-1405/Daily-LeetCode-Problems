class Solution:
    result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        # null case
        if nums is None:
            return self.result
        
        self.helper(nums, 0, [])
        return self.result
    
    # brute force
#     def helper(self, nums, idx, path):
#         # base case
#         if idx == len(nums):
#             temp = path.copy()
#             self.result.append(temp)
#             return
        
#         # logic
#         # not choose
#         self.helper(nums, idx+1, path)
#         # choose
#         path.append(nums[idx]) # action
#         self.helper(nums, idx+1, path) # recurse
#         path.pop() # backtrack

    # using for-loop recursion
    def helper(self, nums, pivot, path):
        # no base case
        self.result.append(path.copy())
        # logic
        for i in range(pivot, len(nums)):
            path.append(nums[i]) # action
            self.helper(nums, i+1, path) # recurse
            path.pop() # backtrack