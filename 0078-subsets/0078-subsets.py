class Solution:
    result = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        # null case
        if nums is None:
            return self.result
        
        self.helper(nums, 0, [])
        return self.result
    
    
    def helper(self, nums, idx, path):
        # base case
        if idx == len(nums):
            temp = path.copy()
            self.result.append(temp)
            return
        
        # logic
        # not choose
        self.helper(nums, idx+1, path)
        # choose
        path.append(nums[idx]) # action
        self.helper(nums, idx+1, path) # recurse
        path.pop() # backtrack