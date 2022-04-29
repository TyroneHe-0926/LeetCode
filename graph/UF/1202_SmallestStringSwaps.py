from collections import defaultdict, deque
from typing import List

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf, res, m = UF(len(s)), [], defaultdict(list)
        for x,y in pairs: 
            uf.union(x,y)
        print(uf.p)
        for i in range(len(s)): 
            m[uf.find(i)].append(s[i])
        print(m)
        for comp_id in m.keys(): 
            m[comp_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)

class Solution:
    """Rewrote it with rank and path compression optimization"""
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        slen, cmap = len(s), defaultdict(list)
        self.root, self.rank, result = [i for i in range(slen)], [1] * slen, [''] * slen
        for p1, p2 in pairs: self.union(p1, p2)
        for i in range(slen): cmap[self.find(self.root[i])].append(s[i])
        for _, letters in cmap.items(): letters.sort(reverse=True)
        print(cmap)
        for i in range(slen): result[i] = cmap[self.find(i)].pop()
        return ''.join(result)
        
    def find(self, node):
        if self.root[node] == node: return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]: self.root[root1] = self.root[root2]
            else: self.root[root2] = self.root[root1]

solution = Solution()
s = "cba"
pairs = [[0,1],[1,2]]
s2 = "dcab" 
pairs2 = [[0,3],[1,2],[0,2]]
s3 = "dcab"
pairs3 = [[0,3],[1,2]]
# print(solution.smallestStringWithSwaps(s, pairs))
print(solution.smallestStringWithSwaps(s2, pairs2))
print(solution.smallestStringWithSwaps(s3, pairs3))