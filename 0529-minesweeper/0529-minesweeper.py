class Solution:
    dirs = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
    # Using BFS
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         # null case
#         if board is None:
#             return board
        
#         m = len(board)
#         n = len(board[0])
        
#         if board[click[0]][click[1]] == "M":
#             board[click[0]][click[1]] = "X"
#             return board
        
#         queue = deque()
#         queue.append(click)
#         board[click[0]][click[1]] = "B"
        
#         while queue:
#             curr = queue.popleft()
#             count = self.count_mines(board, curr[0], curr[1], m, n)
#             if count == 0:
#                 for dirn in self.dirs:
#                     nr = dirn[0] + curr[0]
#                     nc = dirn[1] + curr[1]
#                     if nr>=0 and nr<m and nc>=0 and nc<n and board[nr][nc] == "E":
#                         queue.append([nr, nc])
#                         board[nr][nc] = "B"
#             else:
#                 board[curr[0]][curr[1]] = str(count)
#         return board
    
    # Using DFS
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # null case
        if board is None:
            return board
        
        m = len(board)
        n = len(board[0])
        
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board 
        
        def dfs(board, i, j, m, n):
            # base case
            if i<0 or i==m or j<0 or j==n or board[i][j] != "E":
                return

            # logic
            board[i][j] = "B"
            count = self.count_mines(board, i, j, m, n)
            if count == 0:
                for dirn in self.dirs:
                    nr = dirn[0] + i
                    nc = dirn[1] + j
                    dfs(board, nr, nc, m, n)
            else:
                board[i][j] = str(count)
        
        dfs(board, click[0], click[1], m, n)
        return board
    
    
    def count_mines(self, board, i, j, m, n):
        count = 0
        for dirn in self.dirs:
            nr = dirn[0] + i
            nc = dirn[1] + j
            if nr>=0 and nr<m and nc>=0 and nc<n and board[nr][nc] == "M":
                count += 1
        return count