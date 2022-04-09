from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        values = defaultdict(list)
        def traverse(node: Optional[TreeNode], height: int):
            if not node:
                return
            values[height].append(node.val)
            traverse(node.left, height+1)
            traverse(node.right, height+1)
        traverse(root, 0)
        return [round(sum(values[i])/len(values[i]), 5) for i in values]
            

solution = Solution()
n9 = TreeNode(val=9)
n15 = TreeNode(val=15)
n7 = TreeNode(val=7)
n20 = TreeNode(val=20, left=n15, right=n7)
root = TreeNode(val=3, left=n9, right=n20)
print(solution.averageOfLevels(root))