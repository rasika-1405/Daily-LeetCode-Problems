# creating doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.capacity = capacity
        
            
    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next


    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.remove_node(node)
        self.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # not a fresh node
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove_node(node)
            self.add_to_head(node)
        else:
            # check capacity
            if len(self.map) == self.capacity:
                tail_prev = self.tail.prev
                self.remove_node(tail_prev)
                self.map.pop(tail_prev.key)
            new_node = Node(key, value)
            self.add_to_head(new_node)
            self.map[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)