from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        value, values = [], []
        def dfs(node: Optional[TreeNode]):
            if not node.right and not node.left:
                value.append(node.val)
                return True
            if node.left:
                if dfs(node.left):  node.left = None
            if node.right:
                if dfs(node.right): node.right = None
    
        while root.left or root.right:
            dfs(root)
            values.append(value)
            value = []
        values.append([root.val])

        return values

"""
O(n) with dict on Leetcode
class Solution(object):
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret
"""
solution = Solution()
node5 = TreeNode(val=5, left=TreeNode(val=8))
node4 = TreeNode(val=4)
node3 = TreeNode(val=3)
node2 = TreeNode(val=2, left=node4, right=node5)
root = TreeNode(val=1, left=node2, right=node3)
print(solution.findLeaves(root))

root2 = TreeNode(val=1)
print(solution.findLeaves(root))