# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # iterative method
#         st1 = []  #stack for current node
#         st2 = []   # number
        
#         curr_num = 0
#         result = 0
        
#         while root != None or len(st1) != 0:
#             while root != None:
#                 curr_num = curr_num * 10 + root.val
#                 st1.append(root)
#                 st2.append(curr_num)
#                 root = root.left
                
#             root = st1.pop()
#             curr_num = st2.pop()
            
#             if root.left == None and root.right == None:
#                 result += curr_num
#             root = root.right

        # recursive method
        self.helper(root, 0)
        return self.result

    def helper(self, root, curr_num):
        # base case
        if root == None:
            return
        # check leaf condition
        if root.left == None and root.right == None:
            self.result += curr_num * 10 + root.val
        
        self.helper(root.left, curr_num * 10 + root.val)
        self.helper(root.right, curr_num * 10 + root.val)
        