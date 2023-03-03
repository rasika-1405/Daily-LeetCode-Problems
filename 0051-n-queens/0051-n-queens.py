class Solution:
    m = 0
    result = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.result = []
        self.m = n
        board = [[False for _ in range(n)] for _ in range(n)]
        self.backtrack(board, 0)
        return self.result
    
    
    def backtrack(self, board, r):
        # base case
        if r == self.m:
            res = []
            for i in range(self.m):
                temp = []
                for j in range(self.m):
                    if board[i][j]:
                        temp.append("Q")
                    else:
                        temp.append(".")
                res.append("".join(temp))
            self.result.append(res)
                
        
        #logic
        # check safe column
        for c in range(self.m):
            if (self.isSafe(board, r, c)):
                board[r][c] = True # action
                self.backtrack(board, r+1) # recurse
                board[r][c] = False # backtrack
        

    def isSafe(self, board, r, c):
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
        while i>=0 and j<self.m:
            if board[i][j]:
                return False
            i -= 1
            j += 1

        return True