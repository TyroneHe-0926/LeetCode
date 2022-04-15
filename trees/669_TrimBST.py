from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root.val == high:
            root.right = None
            if root.left: root.left = self.trimBST(root.left, low, high)
        elif root.val > high:
            root.right = None
            if root.left:
                root.val = root.left.val
                root.right = root.left.right
                root.left = root.left.left
                root = self.trimBST(root, low, high)
            else:
                return None
        elif root.val == low:
            root.left = None
            if root.right: root.right = self.trimBST(root.right, low, high)
        elif root.val < low:
            root.left = None
            if root.right:
                root.val = root.right.val
                root.left = root.right.left
                root.right = root.right.right
                root = self.trimBST(root, low, high)
            else: 
                return None
        elif root.val > low and root.val < high:
            if root.left: root.left = self.trimBST(root.left, low, high)
            if root.right: root.right = self.trimBST(root.right, low, high)
        
        return root

class Solution():
    def trimBST(self, root, low, high):
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)

solution = Solution()
root = TreeNode(val=4, left=TreeNode(val=3))
print(solution.trimBST(root, 1,2))