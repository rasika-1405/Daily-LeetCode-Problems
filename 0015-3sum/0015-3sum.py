class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # null case
        if nums is None:
            return []
        
        n = len(nums)
        
        # brute force
        
#         result_set = set()
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 for k in range(j+1, n):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         result = [nums[i], nums[j], nums[k]]
#                         result = sorted(result)
#                         result = tuple(result)
#                         result_set.add(result)
                        
                        
        # using two pointers
        
        result = []
        nums = sorted(nums)
        for i in range(n-2):
            if nums[i] > 0:
                break
            # outside duplicacy
            if i!=0 and nums[i] == nums[i-1]:
                continue
            low = i+1
            high = n-1
            
            while low<high:
                total = nums[i] + nums[low] + nums[high]
                if total == 0:
                    l1 = [nums[i], nums[low], nums[high]]
                    result.append(l1)
                    low +=1
                    high -= 1
                    
                    # inner duplicacy
                    while low<high and nums[low] == nums[low-1]:
                        low += 1
                    while low<high and nums[high] == nums[high+1]:
                        high -= 1
                elif total > 0:
                    high -= 1
                else:
                    low += 1
            
                        
        return result
                        
        