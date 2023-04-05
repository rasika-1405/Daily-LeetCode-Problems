class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # null case
        if nums is None:
            return [-1]
        
        n = len(nums)
        result = [-1 for _ in range(n)]
        stk = []
        
        for i in range(2*n):
            while stk and nums[i%n] > nums[stk[-1]]:
                curr = stk.pop()
                result[curr] = nums[i%n]
            if i<n:
                stk.append(i)
        
        return result