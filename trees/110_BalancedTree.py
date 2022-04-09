from turtle import left, right
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    balanced = None
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        def check_height(node: Optional[TreeNode], height):
            if not node: return 0
            left = check_height(node.left, height)
            right = check_height(node.right, height)
            if abs(left-right) > 1: self.balanced = False
            return max(left, right) + 1
        check_height(root, 0)
        return self.balanced

solution = Solution()
root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=3)), right=TreeNode(val=2))
print(solution.isBalanced(root))