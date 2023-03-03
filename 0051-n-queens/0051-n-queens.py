class Solution:
    # m = 0
    # result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        m = n
        board = [[False for _ in range(n)] for _ in range(n)]
#         backtrack(board, 0)
#         return self.result
    
    
        def backtrack(board, r):
            # base case
            if r == m:
                res = []
                for i in range(m):
                    temp = []
                    for j in range(m):
                        if board[i][j]:
                            temp.append("Q")
                        else:
                            temp.append(".")
                    res.append("".join(temp))
                result.append(res)


            #logic
            # check safe column
            for c in range(m):
                if (isSafe(board, r, c)):
                    board[r][c] = True # action
                    backtrack(board, r+1) # recurse
                    board[r][c] = False # backtrack


        def isSafe(board, r, c):
            # same column
            for i in range(r):
                if board[i][c]:
                    return False
            #upper left
            i,j = r,c
            while i>=0 and j>=0:
                if board[i][j]:
                    return False
                i -= 1
                j -= 1

            #upper right
            i,j = r,c
            while i>=0 and j<m:
                if board[i][j]:
                    return False
                i -= 1
                j += 1

            return True
        
        backtrack(board, 0)
        return result