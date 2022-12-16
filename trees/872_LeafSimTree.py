from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []
        self.getLeafs(root1, leaf1)
        self.getLeafs(root2, leaf2)
        
        if(len(leaf1) != len(leaf2)): return False

        for i, val in enumerate(leaf1):
            if leaf2[i] != val: return False
        
        return True


    def getLeafs(self, root: Optional[TreeNode], leafs: list):
        if not root: return
        if not root.left and not root.right:
            leafs.append(root.val)
            return
        self.getLeafs(root.left, leafs)
        self.getLeafs(root.right, leafs)
