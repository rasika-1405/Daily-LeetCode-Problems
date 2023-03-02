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
            self.result.append(path)
            return
        
        # logic
        self.helper(nums, idx+1, path.copy()) # not choose
        temp = path.copy()
        temp.append(nums[idx])
        self.helper(nums, idx+1, temp) # choose