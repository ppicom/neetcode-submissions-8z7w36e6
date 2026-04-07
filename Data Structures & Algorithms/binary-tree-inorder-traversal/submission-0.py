# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_traversal = []

        inorder(root, inorder_traversal)

        return inorder_traversal

def inorder(root: Optional[TreeNode], lst: List[int]):
    if not root:
        return
    
    inorder(root.left, lst)
    lst.append(root.val)
    inorder(root.right, lst)