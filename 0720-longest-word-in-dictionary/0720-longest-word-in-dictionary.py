class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        self.word = ""

        
class Solution:
    def __init__(self):
        self.root = None

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            char = word[i]
            if curr.children[ord(char) - ord('a')] == None:
                curr.children[ord(char) - ord('a')] = TrieNode()
            curr = curr.children[ord(char) - ord('a')]
        curr.is_end = True
        curr.word = word
        
    
    def longestWord(self, words: List[str]) -> str:
        self.root = TrieNode()
        for word in words:
            self.insert(word)
        
        queue = deque([self.root])
        curr = self.root
        
        while queue:
            curr = queue.popleft()
            for i in range(25,-1, -1):
                if curr.children[i] != None and curr.children[i].is_end:
                    queue.append(curr.children[i])
        return curr.word
        