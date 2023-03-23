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
        node_map = {}
        def clone(node):
            if node is None:
                return None
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            return new_node
            
        copy_head = clone(head)
        curr = head
        copy_curr = copy_head
        
        while curr:
            copy_curr.next = clone(curr.next)
            copy_curr.random = clone(curr.random)
            curr = curr.next
            copy_curr = copy_curr.next
        
        return copy_head