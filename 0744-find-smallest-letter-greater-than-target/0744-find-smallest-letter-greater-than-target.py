class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # null case
        if letters is None:
            return ""
        
        # binary search
        low = 0
        high = len(letters)-1
        
        while low<=high:
            mid = low+(high-low) // 2
            if letters[mid-1] <= target <letters[mid]:
                return letters[mid]
            elif letters[mid] <= target:
                low = mid+1
            else:
                high = mid-1
        return letters[0]