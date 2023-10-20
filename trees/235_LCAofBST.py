# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    lowest = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        low, high = None, None
        if p.val < q.val:
            low, high = p, q
        else:
            low, high = q, p
        self.traverse(root, low, high)
        return self.lowest


    def traverse(self, node: TreeNode, low: TreeNode, high: TreeNode):
        if node.val >= low.val and node.val <= high.val: 
            self.lowest = node
            return
        if node.val < low.val: self.traverse(node.right, low, high)
        if node.val > high.val: self.traverse(node.left, low, high)
