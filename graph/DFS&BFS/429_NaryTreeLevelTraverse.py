from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level_traversed = []    
        if not root:
            return []

        queue = [root]
        next_layer = root.children
        level_traversed.append([root.val])

        while queue:

            node = queue.pop(0)
    
            if not node:
                continue
            
            for child in node.children:
                queue.append(child)
            
            if queue == next_layer:
                if queue:
                    level_traversed.append([n.val for n in queue])
                next_layer = []
                for next_node in queue:
                    for child in next_node.children:
                        if child:
                            next_layer.append(child)
    
        return level_traversed
