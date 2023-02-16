# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper(root, path, curr_sum, target):
            # base case
            if root == None:
                return
            
            # logic
            curr_sum += root.val
            # temp = path
            # print(temp)
            path.append(root.val)
            if root.left == None and root.right == None:
                if curr_sum == target:
                    path_copy = path.copy()
                    self.result.append(path_copy)
            helper(root.left, path, curr_sum, target)
            helper(root.right, path, curr_sum, target)
            path.pop()
        
        self.result = []
        helper(root, [], 0, targetSum)
        return self.result
    
    