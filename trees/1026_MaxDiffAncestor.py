from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_diff = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        path = []

        self.dfs(root, path)

        return self.max_diff
        
    def dfs(self, node: TreeNode, path: list):
        path.append(node)
        if not node.left and not node.right:
            self.max_diff = max(self.get_max_diff(path), self.max_diff)
            path.pop()
            return
        
        if node.left: self.dfs(node.left, path)
        if node.right: self.dfs(node.right, path)

        self.max_diff = max(self.get_max_diff(path), self.max_diff)
        path.pop()
    
    def get_max_diff(self, path):
        last_node, max_diff = path[-1], 0

        for node in path: max_diff = max(abs(node.val - last_node.val), max_diff)

        return max_diff
        