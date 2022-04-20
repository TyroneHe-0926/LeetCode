from typing import Optional
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def traverse(node: TreeNode):
            if node and node.left: traverse(node.left)
            if node:
                if len(heap) < k: heapq.heappush(heap, -node.val)
                elif len(heap) == k and node.val < -min(heap): 
                    heapq.heappop(heap)
                    heapq.heappush(heap, -node.val)
            if node and node.right: traverse(node.right)
        traverse(root)
        return -heap[0]