# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Top-Down approach
        
#         def height(root):
#             if root is None:
#                 return -1
#             return 1 + max(height(root.left), height(root.right))
        
#         # empty tree
#         if root is None:
#             return True
        
#         return abs(height(root.left)-height(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        # Bottom-Up approach
        def helper(root):
            if root is None:
                return True, -1
            left_balanced, left_height = helper(root.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = helper(root.right)
            if not right_balanced:
                return False, 0
            return abs(left_height-right_height)<2, 1+max(left_height,right_height)
        
        
        return helper(root)[0]