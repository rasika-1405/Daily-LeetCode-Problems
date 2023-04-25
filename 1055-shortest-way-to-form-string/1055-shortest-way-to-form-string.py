class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sl = len(source)
        tl = len(target)
        count = 1
        
        sp, tp = 0, 0
        char_set = set()
        for char in source:
            char_set.add(char)
            
        while tp<tl:
            s_char = source[sp]
            t_char = target[tp]
            if t_char not in char_set:
                return -1
            if s_char == t_char:
                sp+=1
                tp+=1
                if tp == tl:
                    return count
            else:
                sp+=1
            if sp == sl:
                count += 1
                sp=0
        return count