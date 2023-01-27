class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0:
            return False
        n = len(matrix) #rows
        m = len(matrix[0]) #cols
        low = 0
        high = m*n-1
        while low<=high:
            mid = low+(high-low)//2
            r = mid//m
            c = mid%m
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                high = mid-1
            else:
                low = mid+1
        return False
        