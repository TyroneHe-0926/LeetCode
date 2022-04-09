class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ppath = []
        while p:
            ppath.append(p)
            p = p.parent
        
        while q:
            if q in ppath: return q
            else: q = q.parent

"""
BFS with better O(h) solution, not always back to root
		seen = set()
        queue = collections.deque([p,q])
        
        while queue:
            curr = queue.popleft()

            if curr in seen:
                return curr

            seen.add(curr)

            if curr.parent:
                queue.append(curr.parent)
                
        return p
"""

"""
 #method2: O(n) time, but O(1) space, The distance of p will travel from p->LCA + LCA->root + q->LCA; q will travel from q->LCA + LCA->root + p->LCA, so at the 2nd pass, they must meet each other at LCA.
    oriP, oriQ = p, q
    while p!=q:
        p=p.parent if p.parent else oriQ
        q=q.parent if q.parent else oriP
    return p #(p meets q at LCA node)		
"""