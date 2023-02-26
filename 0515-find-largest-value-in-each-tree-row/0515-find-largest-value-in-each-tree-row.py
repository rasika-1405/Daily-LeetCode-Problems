# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# arr = [1,2,3,4]
# max = -inf
# for i in range(len(arr)):
#     max = max(arr[i], max)
# return max
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # null case 
        if root is None:
            return result
        
        queue = deque([root])
        
        while queue:
            level = len(queue)
            max_val = -inf
            for i in range(level):
                curr = queue.popleft()
                max_val = max(curr.val, max_val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(max_val)
            
        return result
                