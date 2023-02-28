class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # null case
        if matrix is None:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        # two pointers i & j starting from top right corner
        i, j = 0, (n-1)
        
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False