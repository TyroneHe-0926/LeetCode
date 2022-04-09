# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        head, other = (list1, list2) if list2.val < list1.val else (list2, list1)

        while head:
            self.insert(head.val, other)
            head = head.next
        
        return other


    def insert(self, number, head: Optional[ListNode]):
        while head.next:
            if head.next.val >= number:
                tempnode = ListNode(val=number, next=head.next)
                head.next = tempnode
                return
            head = head.next
        tempnode = ListNode(val=number, next=None)
        head.next = tempnode