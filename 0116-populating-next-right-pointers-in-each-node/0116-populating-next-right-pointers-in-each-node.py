"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        
        # Using BFS - queue
        # queue = deque([root])
        # while queue:
        #     size = len(queue)
        #     prev = None
        #     for i in range(size):
        #         curr = queue.popleft()
        #         if i!= 0:
        #             prev.next = curr
        #         if curr.left:
        #             queue.append(curr.left)
        #             queue.append(curr.right) #complete binary tree
        #         prev = curr
                
        # optimized BFS
        # level = root
        # while level.left:
        #     curr = level
        #     while curr:
        #         curr.left.next = curr.right
        #         if curr.next:
        #             curr.right.next = curr.next.left
        #         curr = curr.next
        #     level = level.left
        
        # using DFS
        def dfs1(left, right):
            # base case
            if left is None:
                return
            
            # logic
            left.next = right
            dfs1(left.left, left.right)
            dfs1(left.right, right.left)
            dfs1(right.left, right.right)
            
        def dfs2(root):
            # base case
            if root.left is None:
                return
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            dfs2(root.left)
            dfs2(root.right)
        
        # dfs1(root.left, root.right)
        dfs2(root)
        
        return root
                