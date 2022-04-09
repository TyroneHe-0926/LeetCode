from turtle import left, right
from typing import Optional, List
from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # My approach is O(NlogN with the sorting of height and sorting at the end)
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelmap = defaultdict(list)
        def traverse(node: Optional[TreeNode], level: int, height: int):
            if not node: return
            levelmap[level].append({
                "val": node.val,
                "height": height
            })
            levelmap[level].sort(key = lambda x: x["height"])
            traverse(node.left, level-1, height+1)
            traverse(node.right, level+1, height+1)
        traverse(root, 0, 0)
        levelmap = dict(sorted(levelmap.items(), key=lambda x: x[0]))
        return [[item["val"] for item in levelmap[level]] for level in levelmap]

class BFSSolution:
    """LC solution using BFS with a queue to prevent sorting, hence O(N)"""
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)
        min_column = max_column = 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                columnTable[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [columnTable[x] for x in range(min_column, max_column + 1)]

s = Solution()
root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
print(s.verticalOrder(root))
root = TreeNode(val=3, left=TreeNode(val=9, left=TreeNode(val=4), right=TreeNode(val=0, right=TreeNode(val=2))), right=TreeNode(val=8, left=TreeNode(val=1, left=TreeNode(val=5)), right=TreeNode(val=7)))
print(s.verticalOrder(root))
root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=6)), right=TreeNode(val=3, left=TreeNode(val=5), right=TreeNode(val=7)))
print(s.verticalOrder(root))