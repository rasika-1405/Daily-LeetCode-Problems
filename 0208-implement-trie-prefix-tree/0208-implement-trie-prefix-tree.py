class TrieNode:
        def __init__(self):
            self.is_end = False
            self.children = [None for _ in range(26)]
    
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            if curr.children[ord(char) - ord('a')] == None:
                curr.children[ord(char) - ord('a')] = TrieNode()
            curr = curr.children[ord(char) - ord('a')]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            if curr.children[ord(char) - ord('a')] == None:
                return False
            curr = curr.children[ord(char) - ord('a')]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            char = prefix[i]
            if curr.children[ord(char) - ord('a')] == None:
                return False
            curr = curr.children[ord(char) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)