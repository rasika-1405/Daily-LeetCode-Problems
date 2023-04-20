class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        result = []
        # null case
        if connections is None:
            return result
        
        discovery = [-1 for _ in range(n)]
        lowest = [0 for _ in range(n)]
        graph = []
        time = 0
        
        def build_graph(connections, n):
            for i in range(n):
                graph.append([])
            for edge in connections:
                graph[edge[0]].append(edge[1])
                graph[edge[1]].append(edge[0])
            
        def dfs(v, u):
            nonlocal time
            # base case
            if discovery[v] != -1:
                return
            
            # logic
            discovery[v] = time
            lowest[v] = time
            time += 1
            
            for n in graph[v]:
                if n == u:
                    continue
                dfs(n, v)
                if lowest[n] > discovery[v]:
                    result.append([n, v])
                lowest[v] = min(lowest[v], lowest[n])
                
        build_graph(connections, n)
        dfs(0, 0)
        return result