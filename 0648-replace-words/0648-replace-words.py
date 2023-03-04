class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]
        
class Solution:
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

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        self.root = TrieNode()
        for string in dictionary:
            self.insert(string)
        
        result = ""
        str_arr = sentence.split()
        
        for k in range(len(str_arr)):
            if k!=0:
                result += " "
            word = str_arr[k]
            replacement = ""
            curr = self.root
            for i in range(len(word)):
                char = word[i]
                if curr.children[ord(char) - ord('a')] == None or curr.is_end:
                    break
                replacement += char
                curr = curr.children[ord(char) - ord('a')]
            if curr.is_end:
                result += replacement
            else:
                result += word
        
        return result