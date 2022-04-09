# Definition for a Node.
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
                
        if not root:
            return None
        
        if not root.left and not root.right:
            return root

        root.next = None
        queue = [root]
        next_layer = [root.left, root.right]

        while queue:

            node = queue.pop(0)
    
            if not node:
                continue
    
            queue.append(node.left)
            queue.append(node.right)
            
            if queue == next_layer:
                for index, n in enumerate(queue):
                    if index+1 == len(queue):
                        n.next = None
                    else:
                        n.next = queue[index+1]
                next_layer = []
                for next_node in queue:
                    if next_node.left:
                        next_layer.append(next_node.left)
                        next_layer.append(next_node.right)
    
        return root
