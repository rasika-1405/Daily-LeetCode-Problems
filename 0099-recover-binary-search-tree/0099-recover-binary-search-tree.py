# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    first, second, prev = None, None, None
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(root):
            # base case
            if root is None:
                return
            
            # logic
            inorder(root.left)
            if self.prev != None and self.prev.val >= root.val:
                #first breach
                if self.first is None:
                    self.first = self.prev
                    self.second = root
                #second breach
                else:
                    self.second = root
            self.prev = root
            inorder(root.right)

        if root is None:
            return
             
        inorder(root)
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp
        
        
        