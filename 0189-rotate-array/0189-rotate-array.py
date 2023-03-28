class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # null case
        if nums is None:
            return 
        
        n= len(nums)
        
        # if k is greater than length of list
        if k >= n:
            k = k%n
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def reverse(nums, left, right):
            while left <= right:
                swap(nums, left, right)
                left+=1
                right-=1
        
            
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
        