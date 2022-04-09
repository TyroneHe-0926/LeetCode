from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def find_max_depth(node, depth):
            if not node:
                return
            self.depth = max(self.depth, depth)
            find_max_depth(node.left, depth+1)
            find_max_depth(node.right, depth+1)
        find_max_depth(root, 1)
        return self.depth

s = Solution()
print(s.maxDepth(None))