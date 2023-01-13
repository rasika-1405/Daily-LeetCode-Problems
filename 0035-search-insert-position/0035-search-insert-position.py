class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # using binary search
        low = 0
        high = len(nums) - 1
        
        while low<=high:
            if (low+high) % 2 == 0:
                mid = (low+high)//2
            else:
                mid = (low+high-1)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if low == high:
                    return mid+1
                low = mid+1
            else:
                if low == high:
                    return mid
                high = mid