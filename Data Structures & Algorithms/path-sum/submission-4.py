# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """bfs explores the tree level by level. We use a queue to store each node along with the remaining sum needed. When we reach a leaf, we check if the target has been met. BFS guarantees we explore all paths systematically."""
        if not root:
            return False
        
        queue = deque([(root, targetSum - root.val)])
        while queue:
            node, curr_sum = queue.popleft()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.left:
                queue.append((node.left, curr_sum - node.left.val))
            if node.right:
                queue.append((node.right, curr_sum - node.right.val))
            
        return False