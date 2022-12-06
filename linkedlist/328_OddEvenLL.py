from typing import Optional
from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        if not head.next: return head

        oddmap, evenmap = defaultdict(ListNode), defaultdict(ListNode)

        temp, index = head.next, 2

        while(temp):
            if index % 2: oddmap[index] = temp
            else: evenmap[index] = temp
            temp = temp.next
            index += 1

        res = head
        temp = res
        for _,v in oddmap.items():
            temp.next = v
            temp = temp.next
        
        for _,v in evenmap.items():
            temp.next = v
            temp = temp.next
        
        temp.next = None
        return res

def printList(head):
    temp = head
    while(temp):
        print(temp.val)
        temp = temp.next

s = Solution()
node5 = ListNode(val = 5, next=None)
node4 = ListNode(val = 4, next=node5)
node3 = ListNode(val = 3, next=node4)
node2 = ListNode(val = 2, next=node3)
head = ListNode(val = 1, next=node2)
printList(s.oddEvenList(head))