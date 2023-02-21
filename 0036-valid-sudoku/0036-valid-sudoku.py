class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # null case
        if board is None:
            return False
        
        set_rows = [set() for _ in range(9)]
        set_cols = [set() for _ in range(9)]
        grid_map = {}
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in set_rows[r] or board[r][c] in set_cols[c]:
                    return False
                set_rows[r].add(board[r][c])
                set_cols[c].add(board[r][c])
                
                # check if grid coordinates exists
                if (r//3, c//3) not in grid_map:
                    grid_map[(r//3, c//3)] = set()
                if board[r][c] in grid_map[(r//3, c//3)]:
                    return False
                grid_map[(r//3, c//3)].add(board[r][c])
                
        return True