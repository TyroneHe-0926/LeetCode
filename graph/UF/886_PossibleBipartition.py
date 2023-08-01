from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        for groups in dislikes:
            self.union(groups[0]-1, groups[1]-1)
        print(self.root)
        return len(set(self.root)) == 2

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]:
                self.root[root1] = self.root[root2]
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = self.root[root1]
            else:
                self.root[root2] = self.root[root1]
                self.rank[root1] += 1

    def find(self, node):
        if self.root[node] == node: return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]