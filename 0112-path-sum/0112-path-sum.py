# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, curr_sum, target):
            # base case
            if root == None:
                return False
            
            curr_sum += root.val
            if root.left == None and root.right == None:
                if curr_sum == target:
                    return True
            
            return helper(root.left, curr_sum, target) or helper(root.right, curr_sum, target)            
            
        return helper(root, 0, targetSum)