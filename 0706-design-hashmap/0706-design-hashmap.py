class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

class MyHashMap:
        
    def __init__(self):
        self.storage = [Node(-1,-1) for _ in range(10000)]
        
    def hash_funct(self, key):
        return key % 10000
    
    def find(self, start, end):
        prev = None
        curr = start
        while curr != None and curr.key != end:
            prev = curr
            curr = curr.next
        return prev
        

    def put(self, key: int, value: int) -> None:
        hash = self.hash_funct(key)
        prev = self.find(self.storage[hash], key)
        if prev.next is None:
            prev.next = Node(key, value)
        else:
            prev.next.value = value
        

    def get(self, key: int) -> int:
        hash = self.hash_funct(key)
        prev = self.find(self.storage[hash], key)
        if prev.next is None:
            return -1
        return prev.next.value
        

    def remove(self, key: int) -> None:
        hash = self.hash_funct(key)
        prev = self.find(self.storage[hash], key)
        if prev.next is not None:
            prev.next = prev.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)