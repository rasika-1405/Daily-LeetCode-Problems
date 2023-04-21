class Solution:
    def expand(self, s: str) -> List[str]:
        result = []
        # null case
        if s is None:
            return result
        
        blocks = []
        i = 0
        while i < len(s):
            block = []
            char = s[i]
            if char == "{":
                i+=1
                while s[i] != "}":
                    if s[i] != ",":
                        block.append(s[i])
                    i+=1
            else:
                block.append(char)
            i+=1
            block.sort()
            blocks.append(block)
        
        def backtrack(blocks, idx, s):
            # base case
            if idx == len(blocks):
                result.append(s)
                return
            
            # logic
            block = blocks[idx]
            for i in range(len(block)):
                char = block[i]
                s+=char #action
                backtrack(blocks, idx+1, s) #recurse
                s = s[:-1] #backtrack
            
        backtrack(blocks, 0, "")
        return result
        