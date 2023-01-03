class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return 0
        two_sum = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    two_sum.append([i,j])
        return two_sum[0]