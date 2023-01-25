class MyHashSet:

    def __init__(self):
        self.bucket = 1000
        self.bucket_items = 1000
        self.hash_storage = [None for _ in range(self.bucket)]
        
    def hash_funct1(self, item):
        return item % 1000
        
    def hash_funct2(self, item):
        return item // 1000

    def add(self, key: int) -> None:
        hash1 = self.hash_funct1(key)
        hash2 = self.hash_funct2(key)
        if self.hash_storage[hash1] == None:
            if hash1 == 0:
                self.hash_storage[hash1] = [False for _ in range(self.bucket_items+1)]
            else:
                self.hash_storage[hash1] = [False for _ in range(self.bucket_items)]
        self.hash_storage[hash1][hash2] = True
        

    def remove(self, key: int) -> None:
        hash1 = self.hash_funct1(key)
        hash2 = self.hash_funct2(key)
        if self.hash_storage[hash1] == None:
            return
        self.hash_storage[hash1][hash2] = False

    def contains(self, key: int) -> bool:
        hash1 = self.hash_funct1(key)
        hash2 = self.hash_funct2(key)
        if self.hash_storage[hash1] == None:
            return False
        return self.hash_storage[hash1][hash2]
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)