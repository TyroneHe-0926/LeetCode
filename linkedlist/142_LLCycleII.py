from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """Used the Floyd's Tortoise and Hare idea in finding duplicate (287)"""
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tortoise, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare: break
        
        tortoise = head
        while hare and hare.next:
            if tortoise == hare: return tortoise
            tortoise = tortoise.next
            hare = hare.next
        
        return None