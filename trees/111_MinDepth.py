from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([[root]])
        while queue:
            path = queue.popleft()
            node = path[-1]
            if not node.left and not node.right: return len(path)
            if node.left:
                new_path = path.copy()
                new_path.append(node.left)
                queue.append(new_path)
            if node.right: 
                new_path = path.copy()
                new_path.append(node.right)
                queue.append(new_path)
        