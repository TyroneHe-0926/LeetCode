from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: 'TreeNode', target, path: List['TreeNode']):
            path.append(node)
            if node.val == target:
                return True
            if node.left:
                if dfs(node.left, target, path): return True
                else: path.pop()
            if node.right:
                if dfs(node.right, target, path): return True
                else: path.pop()

        ppath, qpath = [], []
        if not dfs(root, p.val, ppath) or not dfs(root, q.val, qpath): return None

        for i in range(len(ppath)-1, -1, -1):
            if i < len(qpath) and ppath[i] in qpath: return qpath[i]