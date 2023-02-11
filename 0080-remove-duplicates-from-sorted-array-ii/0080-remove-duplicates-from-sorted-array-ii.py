class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # null case
        if nums is None:
            return 0
        
        count = 1
        slow = 1
        
        for fast in range(1, len(nums)):
            if nums[fast] == nums[fast-1]:
                count += 1
            else:
                count = 1
            if count <= 2: #can make this generic with "k"
                nums[slow] = nums[fast]
                slow += 1
                
        return slow