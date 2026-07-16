"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        queue = deque([node])

        clones = { node.val: Node(node.val, []) }

        while queue:
            cur = queue.popleft()   
            cur_clone = clones[cur.val]

            if not cur.neighbors:
                continue
            
            for nbr in cur.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    queue.append(nbr)

                cur_clone.neighbors.append(clones[nbr.val])


        return clones[node.val]