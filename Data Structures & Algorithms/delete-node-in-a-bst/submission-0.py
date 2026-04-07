# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return delete(root, key)
        

def min_node(root: Optional[TreeNode]) -> Optional[TreeNode]:
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def delete(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if val > root.val:
        root.right = delete(root.right, val)
    elif val < root.val:
        root.left = delete(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            succ = min_node(root.right)
            root.val = succ.val
            root.right = delete(root.right, succ.val)
    
    return root