class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        temp = bitmask & (-bitmask)
        bitmask2 = 0
        
        for num in nums:
            if temp & num != 0:
                bitmask2 ^= num
        
        return [bitmask2, bitmask^bitmask2]