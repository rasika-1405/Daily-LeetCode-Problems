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
        
#         queue = deque([root])
        
#         while queue:
#             size = len(queue)
#             prev = None
#             for i in range(size):
#                 curr = queue.popleft()
#                 if i!= 0:
#                     prev.next = curr
#                 if curr.left:
#                     queue.append(curr.left)
#                     queue.append(curr.right) #complete binary tree
#                 prev = curr
                
        # optimized BFS
        level = root
        while level.left:
            curr = level
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            level = level.left
        
        return root
                