class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        
        # null case
        if nums is None:
            return result
        
        n = len(nums)
        
        for i in range(n):
            # get index
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
                
        for i in range(n):
            if nums[i] > 0:
                result.append(i+1)
            else:
                nums[i] *= -1
        
        return result