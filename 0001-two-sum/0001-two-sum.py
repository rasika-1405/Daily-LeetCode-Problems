class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        if nums is None or len(nums) == 1:
            return result
        
        # brute force
        
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     result.append([i, j])
        
        # using hashing
        
        sum_map = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in sum_map:
                result.append([sum_map[k], i])
            else:
                sum_map[nums[i]] = i
        
        return result[0]
    
        
    
        