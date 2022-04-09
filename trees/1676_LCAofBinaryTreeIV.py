from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def traverse(node: 'TreeNode'):
            if node in nodes:
                self.lca = node 
                return True
            right = traverse(node.right) if node.right else None
            left = traverse(node.left) if node.left else None
            if (left and right):
                self.lca = node
                return True
        traverse(root)
        return self.lca