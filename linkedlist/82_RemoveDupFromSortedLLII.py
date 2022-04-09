# Definition for singly-linked list.
from typing import Optional
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        nodelist = []
        while head:
            nodelist.append(head.val)
            head = head.next
        count = Counter(nodelist)

        for number in count:
            if count[number] > 1:
                nodelist = list(filter((number).__ne__, nodelist))

        if not nodelist:
            return None

        new_head = ListNode(nodelist[0], None)
        curnode = new_head
        
        for number in nodelist[1:]:
            curnode.next = ListNode(number, None)
            curnode = curnode.next
        
        return new_head

class Solution:
    """Sentinel Head"""
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # sentinel
        sentinel = ListNode(0, head)

        # predecessor = the last node before the sublist of duplicates
        pred = sentinel
        
        while head:
            # if it's a beginning of duplicates sublist skip all duplicates
            if head.next and head.val == head.next.val:
                # move till the end of duplicates sublist
                while head.next and head.val == head.next.val:
                    head = head.next
                # skip all duplicates
                pred.next = head.next 
            # otherwise, move predecessor
            else:
                pred = pred.next 
                
            # move forward
            head = head.next
            
        return sentinel.next