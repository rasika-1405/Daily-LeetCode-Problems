class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) == 0:
            return [-1, -1]
        n = len(nums)
        if nums[0] > target or nums[n-1] < target:
            return [-1,-1]
        
        first = self.binary_search_first(nums, target)
        if first == -1:
            return [-1,-1]
        # slicing will take extra space as it creates another list
        second = self.binary_search_last(nums, first, n-1, target)
        return [first, second]
    
    def binary_search_first(self, nums, target):
        low = 0
        high = len(nums) -1
        while low <= high:
            mid = low+(high-low) // 2
            if nums[mid] == target:
                if mid == 0 or nums[mid] > nums[mid-1]:
                    return mid
                else:
                    high = mid - 1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid -1
        return -1
    
    def binary_search_last(self, nums, low, high, target):
        while low <= high:
            mid = low+(high-low) // 2
            if nums[mid] == target:
                if mid == len(nums)-1 or nums[mid] < nums[mid+1]:
                    return mid
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid -1
        return -1