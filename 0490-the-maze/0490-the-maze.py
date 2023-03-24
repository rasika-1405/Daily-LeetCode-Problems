class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [[-1,0], [0,1], [1,0], [0,-1]]
        m = len(maze)
        n = len(maze[0])
        
        # null case
        if maze is None:
            return False
        
        queue = deque([start])
        maze[start[0]][start[1]] = 2 # mark as visited
        
        while queue:
            curr = queue.popleft()
            for dirn in dirs:
                i = curr[0]
                j = curr[1]
                
                while i>=0 and j>=0 and i<m and j<n and maze[i][j] != 1:
                    i+=dirn[0]
                    j+= dirn[1]
                i-= dirn[0]
                j-= dirn[1]
                if maze[i][j] != 2:
                    queue.append([i,j])
                    if i == destination[0] and j == destination[1]:
                        return True
                    maze[i][j] = 2
        return False