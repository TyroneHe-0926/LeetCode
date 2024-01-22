from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodemap = {}
        cur_node, index = head, 1

        while cur_node:
            nodemap[index] = cur_node
            cur_node = cur_node.next
            index += 1

        target_index = index-n
        
        if (target_index-1 not in nodemap) and (target_index+1 not in nodemap): 
            return None
        elif (target_index-1 in nodemap) and (target_index+1 not in nodemap):
            nodemap[target_index-1].next = None
        elif (target_index-1 not in nodemap) and (target_index+1 in nodemap): 
            return nodemap[target_index+1]
        else:
            nodemap[target_index-1].next = nodemap[target_index+1]
        
        return head