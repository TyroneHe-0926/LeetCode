# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.next = next
        self.right = right

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        cur, nlayer = deque([root]), deque([])
        if root.left: nlayer.append(root.left)
        if root.right: nlayer.append(root.right)
        while cur:
            next_tmp = deque([])
            for index, node in enumerate(cur):
                if index + 1 > len(cur)-1: node.next = None
                else: node.next = cur[index+1]
                if node.left: next_tmp.append(node.left)
                if node.right: next_tmp.append(node.right)
            
            cur = nlayer
            nlayer = next_tmp
        return root