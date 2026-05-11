"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    The graph may contain cycles, so we cannot simply copy nodes recursively without remembering what we've already copied.
    To handle this, we use a map (old → new):

    - When we first see a node, we create its copy.
    - If we see the same node again, we reuse the already-created copy.
    - This avoids infinite loops and ensures each node is cloned exactly once.

    Depth First Search (DFS) helps us explore and clone all connected nodes.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None