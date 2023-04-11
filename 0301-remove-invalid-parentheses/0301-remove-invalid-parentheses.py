class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = []
        
        # null case
        if s is None:
            return result
        
        # Using BFS
        def validate_string(t):
            count = 0
            for char in t:
                if char.isalpha():
                    continue
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        
        queue = deque()
        string_set = set()
        queue.append(s)
        string_set.add(s)
        flag = False
        
        while queue and not flag:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if validate_string(curr):
                    result.append(curr)
                    flag = True
                if not flag:
                    for j in range(len(curr)):
                        c = curr[j]
                        if c.isalpha():
                            continue
                        child = curr[:j]+curr[j+1:]
                        if child not in string_set:
                            queue.append(child)
                            string_set.add(child)
        return result
                
                