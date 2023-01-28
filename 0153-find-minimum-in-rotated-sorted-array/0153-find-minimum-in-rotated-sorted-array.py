class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0
        low = 0
        high = len(nums) -1
        
        while low <= high:
            # check if array is already is sorted
            if nums[low] <= nums[high]:
                return nums[low]
            mid = low + (high-low) // 2
            if (mid == 0 or nums[mid] < nums[mid-1]) and (mid == len(nums)-1 or nums[mid] < nums[mid+1]):
                return nums[mid]
            elif nums[low] <= nums[mid]: # left-sorted
                low = mid + 1
            else: # right-sorted
                high = mid - 1
        return 0
        