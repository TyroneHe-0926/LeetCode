from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        values = []
        def traverse(node: Optional[TreeNode]):
            if node:
                if node.val <= high and node.val >= low:
                    values.append(node.val)
                    traverse(node.left)
                    traverse(node.right)
                elif node.val < low:
                    traverse(node.right)
                elif node.val > high:
                    traverse(node.left)
        traverse(root)
        return sum(values)

class IterSolution():
    """Doing too much recursion need to maybe try iter for trees too"""
    def rangeSumBST(self, root, L, R):
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans