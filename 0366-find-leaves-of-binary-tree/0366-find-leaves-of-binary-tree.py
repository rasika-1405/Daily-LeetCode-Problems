# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        # null case
        if root is None:
            return result
        
        def height(root):
            # base case
            if root is None:
                return -1
            
            # logic
            left_h = height(root.left)
            right_h = height(root.right)
            
            curr_h = max(left_h, right_h) + 1
            
            if len(result) == curr_h:
                result.append([])
            
            result[curr_h].append(root.val)
            return curr_h
        
        
        height(root)
        return result