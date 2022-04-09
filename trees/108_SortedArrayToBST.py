from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct_tree(left, right):
            if left > right: return None
            mid = (left+right)//2
            root = TreeNode(val=nums[mid], left=construct_tree(left, mid-1), right=construct_tree(mid+1, right))
            return root
        return construct_tree(0, len(nums)-1)