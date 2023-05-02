# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        
        # void based recursion
        def helper(root, low, high):
            nonlocal result
            # base case
            if root is None:
                return
            
            # logic
            if root.left is not None and root.val>=low:
                helper(root.left, low, high)
            if root.val >= low and root.val <= high:
                result+=root.val
            if root.right is not None and root.val<high:
                helper(root.right, low, high)
        
        # integer based recursion
        def helper2(root, low, high):
            # base case
            if root is None:
                return 0
            
            # logic
            temp, left, right =0, 0,0
            if root.left is not None and root.val>low:
                left = helper2(root.left, low, high)
            if root.val >= low and root.val <= high:
                temp = root.val
            if root.right is not None and root.val<high:
                right = helper2(root.right, low, high)
            return temp+left+right
        
        # Iterative method
        stk = []
        stk.append(root)
        while stk:
            root = stk.pop()
            if root.val >= low and root.val <= high:
                result+=root.val
            if root.right is not None:
                stk.append(root.right)
            if root.left is not None:
                stk.append(root.left)
            
        # return helper2(root, low, high)
        # helper(root, low, high)
        return result