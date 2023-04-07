class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute force
        hash_map = {}
        
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        for num in hash_map:
            if hash_map[num] == 1:
                return num
            