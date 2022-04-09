# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval, qval = p.val, q.val

        def get_lca(node: 'TreeNode'):
            if pval > node.val and qval > node.val: return get_lca(node.right)
            elif pval < node.val and qval < node.val: return get_lca(node.left)
            else: return node
        
        return get_lca(root)