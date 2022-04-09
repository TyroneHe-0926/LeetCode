from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        values = []
        def traverse(node: Optional[TreeNode]):
            if not node.left and not node.right:
                values.append(node.val)
                return
            if node.left:
                traverse(node.left)
            values.append(node.val)
            if node.right:
                traverse(node.right)
        traverse(root)
        return values

"""
             1
           2   3    --> 4 2 5 1 3
          4 5  
"""