class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        
        # Using BFS
#         queue = deque()
#         visited = set()
#         queue.append(0)
#         visited.add(0)
#         jumps = 1
        
#         while queue:
#             size = len(queue)
#             for k in range(size):
#                 i = queue.popleft()
#                 for j in range(nums[i], -1, -1):
#                     new_idx = i+j
#                     if new_idx>=len(nums)-1:
#                         return jumps
#                     if new_idx not in visited:
#                         queue.append(new_idx)
#                         visited.add(new_idx)
#             jumps+=1
#         return 7209

        # Using DFS
#         min_jump = inf
        
#         def dfs(nums, i, jumps):
#             # base case
#             if i>= len(nums)-1:
#                 min_jump = min(min_jump, jumps)
            
#             # logic
#             for j in range(nums[i], -1, -1):
#                 new_idx = i+j
#                 dfs(nums, new_idx, jumps+1)
            
#         dfs(nums, 0, 0)
#         return min_jump

        # Using greedy approach
        curr_interval = nums[0]
        next_interval = nums[0]
        jumps = 1
        
        for i in range(1, len(nums)):
            next_interval = max(next_interval, nums[i]+i)
            if i == curr_interval and i!=len(nums)-1:
                jumps+=1
                curr_interval = next_interval
        
        return jumps