class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]
        
        # null case
        if nums is None:
            return result
        
        rp = 1 # running product
        result[0] = 1
        
        # left pass
        for i in range(1, n):
            rp *= nums[i-1]
            result[i] = rp
            
        # right pass
        rp = 1
        for i in range(n-2, -1, -1):
            rp *= nums[i+1]
            result[i] = rp*result[i]
        
        return result
            