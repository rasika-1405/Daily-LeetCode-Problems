class Solution:
    global dirs
    global m
    global n
    # global board
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.m = len(board)
        self.n = len(board[0])
        
        # null case
        if board is None:
            return
        
        # 1->0 mark as 3
        # 0->1 mark as 2
        self.dirs = [[-1,0], [1,0], [0, -1], [0, 1], [-1,-1], [-1, 1], [1, 1], [1, -1]]
        
        for i in range(self.m):
            for j in range(self.n):
                live_neighbors = self.countAlive(board, i, j)
                if board[i][j] == 1 and (live_neighbors<2 or live_neighbors>3):
                    board[i][j] = 3
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2
                    
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == 3:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1
        
    
    def countAlive(self, board, i, j):
        result = 0
        for direction in self.dirs:
            new_r = i + direction[0]
            new_c = j + direction[1]
            
            if new_r >= 0 and new_c >= 0 and new_r < self.m and new_c < self.n and (board[new_r][new_c] == 1 or board[new_r][new_c] == 3):
                result += 1
        
        return result
        
        
        