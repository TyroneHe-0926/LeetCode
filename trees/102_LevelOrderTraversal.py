from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = defaultdict(list)
        def traverse(node: Optional[TreeNode], height):
            if not node:
                return
            level[height].append(node.val)
            traverse(node.left, height+1)
            traverse(node.right, height+1)
        traverse(root, 0)
        return [level[lvl] for lvl in level]


solution = Solution()
root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
print(solution.levelOrder(root))
root = TreeNode(val=3, left=TreeNode(val=9, left=TreeNode(val=4), right=TreeNode(val=0, right=TreeNode(val=2))), right=TreeNode(val=8, left=TreeNode(val=1, left=TreeNode(val=5)), right=TreeNode(val=7)))
print(solution.levelOrder(root))