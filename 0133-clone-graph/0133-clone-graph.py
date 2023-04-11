"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # null case
        if node is None:
            return None
        
        node_map = {}
        
        # Using BFS
#         queue = deque()
#         queue.append(node)
#         new_node = Node(node.val)
#         node_map[node] = new_node
        
#         while queue:
#             curr = queue.popleft()
#             neighbors = curr.neighbors
#             for neighbor in neighbors:
#                 if neighbor not in node_map:
#                     deep_copy = Node(neighbor.val)
#                     node_map[neighbor] = deep_copy
#                     queue.append(neighbor)
#                 node_map[curr].neighbors.append(node_map[neighbor])
#         return new_node
    
        # Using DFS
        def dfs(node):
            # base case
            
            # logic
            deep_copy = Node(node.val)
            node_map[node] = deep_copy
            for neighbor in node.neighbors:
                if neighbor not in node_map:
                    dfs(neighbor)
                node_map[node].neighbors.append(node_map[neighbor])
                
        dfs(node)
        return node_map[node]