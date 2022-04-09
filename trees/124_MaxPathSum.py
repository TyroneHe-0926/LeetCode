import math
from turtle import left
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxm = -math.inf
        def traverse(node: Optional[TreeNode]):
            # reached the end of a node, update maxm to max(maxm, node.val)
            if not node.left and not node.right:
                self.maxm = max(self.maxm, node.val)
                return node.val
            
            # get the current node's left and right path sum
            left_sum = traverse(node.left) if node.left else 0
            right_sum = traverse(node.right) if node.right else 0

            # update maxm. There are 4 possibilities
            # 1. both left and right path sum of the node is negative, in this case node.val is the biggest
            # 2. left is negative, in this case node.val + rightSum is the biggest
            # 3. right is negative, in this case node.val + leftSum is the biggest
            # 4. both left and right are positive, in this case node.val + leftSum + rightSum is the biggest
            # update maxm to max(maxm, the 4 cases)

            self.maxm = max(self.maxm, node.val+left_sum+right_sum, node.val, node.val+left_sum, node.val+right_sum)

            # return the largest sum of the current node's path according to the first 3 cases
            # here we dont want to include both nodes since we are traversng back, not updating the actual maxm
            return max(node.val+left_sum, node.val+right_sum, node.val)
        
        traverse(root)
        return self.maxm

solution = Solution()
root = TreeNode(val=9, left=TreeNode(val=6), right=TreeNode(val=-3, right=TreeNode(val=-6), left=TreeNode(val=2, left=TreeNode(val=2, right=TreeNode(val=-6),left=TreeNode(val=-6, left=TreeNode(val=-6))))))
print(solution.maxPathSum(root))
root = TreeNode(val=3, left=TreeNode(val=9, left=TreeNode(val=4), right=TreeNode(val=0, right=TreeNode(val=2))), right=TreeNode(val=8, left=TreeNode(val=1, left=TreeNode(val=5)), right=TreeNode(val=7)))
print(solution.maxPathSum(root))