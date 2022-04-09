# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#Floyd's Cycle Finding Algorithm
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

"""
def hasCycle(self, head: Optional[ListNode]) -> bool:
    visited = []
    while head:
        if head in visited:
            return True
        visited.append(head)
        head = head.next
    return False
"""