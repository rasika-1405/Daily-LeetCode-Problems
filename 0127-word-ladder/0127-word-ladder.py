class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # creating adjacency list
        wordmap = defaultdict(list)
        
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                wordmap[pattern].append(word)
        
        # Using BFS
        count = 0
        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)
        count += 1
        
        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if curr == endWord:
                    return count
                for j in range(len(curr)):
                    pattern = curr[:j]+"*"+curr[j+1:]
                    for neighbor in wordmap[pattern]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
            count += 1
        return 0
