class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # null case
        if mat is None:
            return []
        
        m = len(mat)  # rows
        n = len(mat[0])  # cols
        r = 0
        c = 0
        result = [0 for _ in range(m*n)]
        
        direction = 1
        index = 0
        
        while index < len(result):
            result[index] = mat[r][c]
            index += 1
            
            # case up
            if direction == 1:
                if c == n-1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            # case down
            else:
                if r == m-1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1
        
        return result
        
        
            