class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # null case
        if board is None:
            return 0
        
        n = len(board)
        arr = [-1 for _ in range(n*n)]
        idx = 0 # for 1D array
        i, j = n-1, 0
        even = 0
        
        while idx < n*n:
            if board[i][j] != -1:
                arr[idx] = board[i][j] - 1
            idx+=1
            if even%2 == 0:
                j+=1
                if j == n:
                    i-=1
                    j-=1
                    even = 1
            else:
                j-=1
                if j == -1:
                    i-=1
                    j+=1
                    even = 0
        
        queue = deque([0])
        arr[0] = -2 # mark as visited
        moves = 0
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == n*n-1:
                    return moves
                for num in range(1,7):
                    child = curr + num
                    if child < n*n:
                        if arr[child] != -2:
                            if arr[child] == -1:
                                queue.append(child)
                            else:
                                queue.append(arr[child])
                            arr[child] = -2
            moves += 1
        return -1