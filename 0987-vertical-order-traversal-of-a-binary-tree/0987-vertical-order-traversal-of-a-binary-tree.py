# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        # null case
        if root is None:
            return result
        
        queue = deque()
        q = deque()
        tree_map = defaultdict(list)
        
        queue.append(root)
        q.append(0)
        min_col, max_col = 0, 0
        
        while queue:
            size = len(queue)
            temp = defaultdict(list)
            for i in range(size):
                curr = queue.popleft()
                col = q.popleft()
                temp[col].append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    q.append(col-1)
                    min_col = min(min_col, col-1)
                if curr.right:
                    queue.append(curr.right)
                    q.append(col+1)
                    max_col = max(max_col, col+1)
            for key in temp:
                tree_map[key].extend(sorted(temp[key]))
            
        # iterating over map keys
        for i in range(min_col, max_col+1):
            result.append(tree_map[i])
        return result