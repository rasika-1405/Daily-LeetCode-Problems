class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0 for _ in range(n)]
        
        for each_trust in trust:
            indegree[each_trust[0]-1]-=1
            indegree[each_trust[1]-1]+=1
            
        for i in range(len(indegree)):
            if indegree[i] == n-1:
                return i+1
        return -1