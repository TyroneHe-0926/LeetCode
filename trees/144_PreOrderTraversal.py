from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        if not root:
            return values
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            values.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return values

"""
             1
           2   3    --> 1 2 4 5 3
          4 5  
"""