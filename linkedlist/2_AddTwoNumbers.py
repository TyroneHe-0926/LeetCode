from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head, overflow, head1, head2 = ListNode(val=(l1.val+l2.val)%10), (l1.val+l2.val)//10, l1.next, l2.next
        temp_head = sum_head
        while head1 or head2:
            val1, val2 = head1.val if head1 else 0, head2.val if head2 else 0
            digit, overflow = (val1+val2+overflow)%10, (val1+val2+overflow)//10
            temp_head.next = ListNode(val=digit)
            head1, head2, temp_head = head1.next if head1 else None, head2.next if head2 else None, temp_head.next
        if overflow: temp_head.next = ListNode(val=overflow)
        return sum_head
    
    def printList(self, ll):
        temp_node, l = ll, []
        while temp_node:
            l.append(temp_node.val)
            temp_node = temp_node.next
        print(l)


s = Solution()
head1 = ListNode(val=6, next=ListNode(val=2, next=ListNode(val=7)))
head2 = ListNode(val=8, next=ListNode(val=1, next=ListNode(val=5)))
s.addTwoNumbers(head1, head2)
head1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))
head2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))))))
s.addTwoNumbers(head1, head2)