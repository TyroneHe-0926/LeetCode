from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()
        def traverse(node: TreeNode):
            if node.left: traverse(node.left)
            if node: values.add(node.val)
            if node.right: traverse(node.right)
        traverse(root)
        values = sorted(values)
        return values[1] if len(values) >= 2 else -1