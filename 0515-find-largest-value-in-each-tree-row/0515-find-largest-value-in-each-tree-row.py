# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # null case 
        if root is None:
            return result
        
        # BFS
#         queue = deque([root])
        
#         while queue:
#             level = len(queue)
#             max_val = -inf
#             for i in range(level):
#                 curr = queue.popleft()
#                 max_val = max(curr.val, max_val)
#                 if curr.left:
#                     queue.append(curr.left)
#                 if curr.right:
#                     queue.append(curr.right)
#             result.append(max_val)
            
        # DFS
        def DFS(root, depth):
            if root is None:
                return result
            if len(result) <= depth:
                result.append(-inf)
            result[depth] = max(root.val, result[depth])
            DFS(root.left, depth+1)
            DFS(root.right, depth+1)
            
        DFS(root, 0)
        
        return result
