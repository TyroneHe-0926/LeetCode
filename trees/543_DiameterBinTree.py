from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def traverse(node: Optional[TreeNode], height):
            if not node: return 0
            left_height = traverse(node.left, height)
            right_height = traverse(node.right, height)
            self.diameter = max(self.diameter, left_height+right_height)
            return max(left_height, right_height)+1
        traverse(root, 0)
        return self.diameter

root = TreeNode(val=1, left=TreeNode(val=2))
solution = Solution()
print(solution.diameterOfBinaryTree(root))