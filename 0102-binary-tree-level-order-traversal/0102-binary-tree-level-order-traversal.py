# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = []
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        self.result = []
        
        # using BFS
        queue = deque([root])
        while queue:
            size = len(queue)
            temp = []
            for i in range(size):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left != None:
                    queue.append(curr.left)
                if curr.right != None:
                    queue.append(curr.right)
            self.result.append(temp)
        
        # Using DFS
#         def dfs(root, depth):
#             if root is None:
#                 return
#             if depth == len(self.result):
#                 self.result.append([])
#             self.result[depth].append(root.val)
#             dfs(root.left, depth+1)
#             dfs(root.right, depth+1)
            
#         dfs(root, 0)
        return self.result