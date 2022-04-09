from collections import defaultdict
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
        print(m)
        for i in range(len(s)): 
            res.append(m[uf.find(i)].pop())
        return ''.join(res)

if __name__ == "__main__":
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

"""
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        str_len = len(s)
        self.root = [i for i in range(str_len)]
        self.headMarks = []
        self.charMarks = [False] * str_len
        self.rank = [1] * str_len
        result = [0] * str_len

        for pair in pairs:
            swap1 = pair[0]
            swap2 = pair[1]
            self.union(swap1, swap2)
        
        for node in self.root:
            head = self.find(node)
            if head not in self.headMarks:
                current_chars = []
                current_indexes = []
                for i in range(str_len):
                    if not self.charMarks[i]:
                        print(i)
                        if self.find(self.root[i]) == head:
                            current_chars.insert(0, s[i])
                            current_indexes.insert(0, i)
                            self.charMarks[i] = True
                current_chars.sort()
                current_indexes.sort()
                for char,index in zip(current_chars, current_indexes):
                    result[index] = char
                self.headMarks.insert(0, head)
        
        return "".join(result)

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root2] > self.rank[root1]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

    def find(self, node):
        if self.root[node] == node:
            return self.root[node]
        self.root[node] = self.find(self.root[node])
        return self.root[node]
"""