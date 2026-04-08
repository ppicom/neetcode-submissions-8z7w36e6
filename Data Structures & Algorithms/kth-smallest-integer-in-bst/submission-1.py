# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        state = {"count": 0, "result": None}

        def inorder(node):
            if not node:
                return
            if state["result"] is not None:
                return
            
            inorder(node.left)

            state["count"] += 1
            if state["count"] == k:
                state["result"] = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return state["result"]