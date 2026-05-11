"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    """
    The graph can have cycles, so while cloning we must avoid creating duplicate nodes or looping forever.
    Using Breadth First Search (BFS), we explore the graph level by level and keep a map from original nodes to their clones.

    - When a node is first seen, create its clone and store it in the map.
    - For every neighbor, ensure its clone exists, then connect the cloned nodes.
    - The map guarantees each node is cloned only once.
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}
        old_to_new[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in old_to_new:
                    old_to_new[nei] = Node(nei.val)
                    q.append(nei)
                old_to_new[cur].neighbors.append(old_to_new[nei])
        
        return old_to_new[node]