# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        
        def helper(root, low, high):
            nonlocal result
            # base case
            if root is None:
                return
            
            # logic
            helper(root.left, low, high)
            if root.val >= low and root.val <= high:
                result+=root.val
            helper(root.right, low, high)
            
        helper(root, low, high)
        return result