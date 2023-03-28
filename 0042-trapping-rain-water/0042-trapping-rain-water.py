class Solution:
    def trap(self, height: List[int]) -> int:
        # null case
        if height is None:
            return 0
        
        # Brute force
        result = 0
        left, lw = 0, 0
        right, rw = len(height)-1,0
        
        while left<=right:
            if lw<=rw: # process left side
                if height[left] >= lw:
                    lw = height[left]
                else: # trap the water
                    result += (lw-height[left])
                left+=1
            else: # process right side
                if height[right] >= rw:
                    rw = height[right]
                else: # trap the water
                    result += (rw-height[right])
                right-=1
                    
        return result