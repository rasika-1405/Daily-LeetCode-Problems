class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        predicted = (n*n + n)/2
        actual = sum(nums)
        return int(predicted - actual)
        