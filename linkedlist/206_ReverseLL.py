# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curnode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        """
        this is aactually like cancelling out the link forwards then replacing with backwards
        kinda like 
                        4 -> 5 (originaly), we do 4->next->next = 4 
                        which is basically saying 4 -> 5 -> next = 4, so 4 -> 5 -> 4,
                        then unlink 4 -> 5 part which becomes 5 -> 4

                        visually it be like 
                                                4 -/> 5 (remove next link for 4)
                                                4 <- 5  (add next next link for 4 to himself, so the next for 5 now is 4, itself)
        """
        return curnode

""" 
Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curnode = head
        prevnode = None
        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode
            prevnode = curnode
            curnode = nextnode
        return prevnode
"""