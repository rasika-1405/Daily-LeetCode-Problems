class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        # null case
        if board is None:
            return False
        m = len(board)
        n = len(board[0])
        
        
        def backtrack(board, word, i, j, idx):
            # base case
            if idx == len(word):
                return True
            if i<0 or j<0 or i==m or j == n or board[i][j] == "#":
                return False
            
            # logic
            if board[i][j] == word[idx]:
                #action
                char = board[i][j]
                board[i][j] = "#"
                
                #recurse
                for dirn in dirs:
                    nr = i + dirn[0]
                    nc = j + dirn[1]
                    if backtrack(board, word, nr, nc, idx+1):
                        return True
                #backtrack
                board[i][j] = char
                
            return False
        
        
        for i in range(m):
            for j in range(n):
                if backtrack(board, word, i, j, 0):
                    return True
        
        return False
                
        