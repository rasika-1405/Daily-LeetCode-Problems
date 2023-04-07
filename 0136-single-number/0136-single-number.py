class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute force
#         hash_map = {}
        
#         for num in nums:
#             if num in hash_map:
#                 hash_map[num] += 1
#             else:
#                 hash_map[num] = 1
        
#         for num in hash_map:
#             if hash_map[num] == 1:
#                 return num
            
        # Using set
        # return 2* sum(set(nums)) - sum(nums)
    
        # Optimal solution - ExOR
        num = 0
        for i in nums:
            num ^= i
        return num