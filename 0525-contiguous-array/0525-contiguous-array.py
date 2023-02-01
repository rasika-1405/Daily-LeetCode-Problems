class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        array_map = {}
        array_map[0] = -1
        r_sum = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                r_sum -= 1
            else:
                r_sum += 1
            if r_sum in array_map:
                count = max(count, i - array_map[r_sum])
            else:
                array_map[r_sum] = i
        
        return count