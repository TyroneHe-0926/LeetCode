from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''ギリギリ O(n) soln in order traverse to sorted array, and then change node val to sum of all following nodes val'''
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        def in_order_tra(node: TreeNode):
            if node and node.left: in_order_tra(node.left)
            if node: nodes.append(node)
            if node and node.right: in_order_tra(node.right)
        in_order_tra(root)

        for i in range(len(nodes)):
            cursum = 0
            for j in nodes[i:]:
                cursum += j.val
            nodes[i].val = cursum
        return root

class Solution():
    """LC clean recursion O(n)"""
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root is not None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root