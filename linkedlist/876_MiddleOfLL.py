from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head
        curnode, length = head, 0
        while curnode:
            length, curnode = length+1, curnode.next
        curnode, curlength = head, 0
        while curnode:
            curlength, curnode = curlength+1, curnode.next
            if curlength == length // 2: return curnode

class SlowFastPointerSolution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

solution = Solution()
print(solution.middleNode(ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=ListNode(val=6))))))))