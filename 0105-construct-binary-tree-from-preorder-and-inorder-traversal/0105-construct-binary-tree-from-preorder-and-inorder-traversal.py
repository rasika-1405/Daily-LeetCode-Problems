# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # null case
        if len(preorder) == 0:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        index = -1
        
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                index = i
                break
        
        in_left = inorder[:index]
        pre_left = preorder[1:index+1]
        in_right = inorder[index+1:]
        pre_right = preorder[index+1:]
        
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        
        return root