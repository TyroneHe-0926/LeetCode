from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        listlen = self.length(head)
        k1, k2 = k-1, listlen-k
        n1, n2, curnode, count = None, None, head, 0
        while curnode:
            if count == k1:
                n1 = curnode
            if count == k2:
                n2 = curnode
            count += 1
            curnode = curnode.next
        
        n1.val, n2.val = n2.val, n1.val

        return head

    def length(self, node: 'ListNode'):
        llen = 0
        while node:
            llen+=1
            node = node.next
        return llen

class Solution:
    """One pass big brain shit"""
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, frontnode, endnode, curnode = 0, None, None, head
        while curnode:
            count += 1
            if endnode: endnode = endnode.next
            if count == k: frontnode, endnode = curnode, head
            curnode = curnode.next
        frontnode.val, endnode.val = endnode.val, frontnode.val
        return head