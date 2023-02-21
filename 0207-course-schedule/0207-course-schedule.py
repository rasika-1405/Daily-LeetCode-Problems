class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        in_degrees = [0 for _ in range(numCourses)]
        for pre_req in prerequisites:
            in_degrees[pre_req[0]] += 1
            
            # from independent to dependent
            # if pre_req[1] not in adj_list:
            #     adj_list[pre_req[1]] = []
            adj_list[pre_req[1]].append(pre_req[0])
            
        # initial queue
        queue = deque()
        count = 0
        for i in range(numCourses):
            if in_degrees[i] == 0:
                queue.append(i)
                count += 1
        
        if len(queue) == 0:
            return False
        
        while queue:
            curr = queue.popleft()
            children = adj_list[curr] #list
            for child in children:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append(child)
                    count += 1
        return count == numCourses
            