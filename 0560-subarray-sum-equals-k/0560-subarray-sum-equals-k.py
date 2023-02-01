class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        array_map = {}
        array_map[0] = 1 #dummy key,value
        r_sum = 0
        count = 0
        
        for i in range(len(nums)):
            r_sum += nums[i]
            if (r_sum - k) in array_map:
                count = count + array_map[r_sum-k]
            if r_sum not in array_map:
                array_map[r_sum] = 0
            array_map[r_sum] += 1
        return count