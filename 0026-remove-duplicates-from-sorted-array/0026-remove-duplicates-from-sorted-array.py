class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while (i<n-1):
            first = nums[i]
            if nums[i+1] == first:
                nums.remove(nums[i+1])
                n = n-1
            else:
                i = i+1
        return n