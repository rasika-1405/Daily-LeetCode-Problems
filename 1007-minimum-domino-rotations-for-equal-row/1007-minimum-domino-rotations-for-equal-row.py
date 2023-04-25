class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        domino_map = defaultdict(int)
        n = len(tops)
        candidate = -1
        
        for i in range(n):
            top = tops[i]
            domino_map[top] += 1
            cntT = domino_map[top]
            if cntT >= n:
                candidate = top
                break
            bottom = bottoms[i]
            domino_map[bottom] += 1
            cntB = domino_map[bottom]
            if cntB >= n:
                candidate = bottom
                break
            
        if candidate == -1:
            return -1
        
        t_rot, b_rot = 0, 0
        for i in range(n):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1
            if tops[i] != candidate:
                t_rot += 1
            if bottoms[i] != candidate:
                b_rot+=1
        return min(t_rot, b_rot)