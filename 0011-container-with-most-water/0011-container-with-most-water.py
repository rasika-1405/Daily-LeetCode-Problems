class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        
        # brute force
        
#         for i in range(n):
#             for j in range(i+1, n):
#                 max_area = max(max_area, (min(height[i], height[j]) * (j-i)))
                
        # using 2 pointers
        low = 0
        high = n-1
        
        while low < high:
            curr_area = min(height[low], height[high]) * (high-low)
            max_area = max(max_area, curr_area)
            if height[low] <= height[high]:
                low += 1
            else:
                high -= 1
            
        return max_area