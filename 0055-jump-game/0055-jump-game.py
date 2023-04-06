class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1
        if len(nums) < 2:
            return True
        
        dp = [-1 for _ in range(len(nums))]
        
        # Using BFS
#         queue = deque([0])
#         visited = set()
#         visited.add(0)
        
#         while queue:
#             i = queue.popleft()
#             for j in range(nums[i], 0, -1):
#                 new_idx = i+j
#                 if new_idx>=n:
#                     return True
#                 if new_idx not in visited:
#                     queue.append(new_idx)
#                     visited.add(new_idx)
#         return False
        
        # Using DFS
        def dfs(nums, i):
            # base case
            if i>= len(nums)-1:
                return True
            if dp[i] == 2:
                return False
            
            #logic
            maxx = nums[i]
            dp[i] = 1
            for j in range(maxx, 0, -1):
                new_idx = i+j
                if new_idx>=len(nums)-1:
                    return True
                if dp[new_idx] == -1 and dfs(nums, new_idx):
                    return True
            dp[i] = 2
            return False
    
        return dfs(nums, 0)
        
        