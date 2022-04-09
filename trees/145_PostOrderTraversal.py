from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        if not root:
            return values
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            traverse(node.right)
            values.append(node.val)
        traverse(root)
        return values

"""
             1
           2   3    --> 4 5 2 3 1
          4 5  
"""