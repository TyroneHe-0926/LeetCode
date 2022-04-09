from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, placement,level, root, dic):
        if(not root):
            return
        dic[placement].append((level, root.val))
        self.helper(placement-1, level+1, root.left, dic)
        self.helper(placement+1, level+1, root.right, dic)
		
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic = defaultdict(list)
        self.helper(0,0, root, dic)
        result = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                temp.append(j[1])
            result.append(temp)
        return result

s = Solution()
root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=6)), right=TreeNode(val=3, left=TreeNode(val=5), right=TreeNode(val=7)))
print(s.verticalTraversal(root))