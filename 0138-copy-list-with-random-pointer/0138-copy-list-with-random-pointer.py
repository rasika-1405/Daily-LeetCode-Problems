"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
#         node_map = {}
#         def clone(node):
#             if node is None:
#                 return None
#             if node in node_map:
#                 return node_map[node]
#             new_node = Node(node.val)
#             node_map[node] = new_node
#             return new_node
            
#         copy_head = clone(head)
#         curr = head
#         copy_curr = copy_head
        
#         while curr:
#             copy_curr.next = clone(curr.next)
#             copy_curr.random = clone(curr.random)
#             curr = curr.next
#             copy_curr = copy_curr.next

        if head is None:
            return None
        curr = head
        
        # create deep copy of list
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        
        # create random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        # splitting 2 lists
        curr = head
        copy_head = head.next
        copy_curr = copy_head
        
        while curr and copy_curr.next:
            curr.next = curr.next.next
            copy_curr.next = copy_curr.next.next
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_head