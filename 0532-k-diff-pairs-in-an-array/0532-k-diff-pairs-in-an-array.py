class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # null case
        
        if nums is None:
            return []
        
        num_set = set()
        result_set = set()
        n = len(nums)
        
        # x-y = k
        for i in range(n):
            temp1 = k + nums[i]
            temp2 = nums[i] - k
            
            if temp1 in num_set:
                res = sorted([nums[i], temp1])
                res = tuple(res)
                result_set.add(res)
            if temp2 in num_set:
                res = sorted([nums[i], temp2])
                res = tuple(res)
                result_set.add(res)
            num_set.add(nums[i])
            
        return len(result_set)