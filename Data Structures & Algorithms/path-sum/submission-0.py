# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        cumulative = 0

        def path_sum(node, target):
            nonlocal cumulative
            if not node:
                return False
            
            cumulative += node.val

            if not node.left and not node.right and cumulative == target:
                return True
            
            if path_sum(node.left, target):
                return True
            if path_sum(node.right, target):
                return True
            
            cumulative -= node.val
            
            return False
        
        return path_sum(root, targetSum)




