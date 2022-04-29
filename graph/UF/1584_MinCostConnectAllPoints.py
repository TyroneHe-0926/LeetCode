from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        plen, edges, result = len(points), [], 0
        self.root, self.rank = [i for i in range(plen)], [1] * plen
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i+1:]):
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append((i, i+j+1, cost))
        
        edges.sort(key=lambda x: x[2])

        for p1, p2, cost in edges:
            if self.connected(p1, p2): continue
            self.union(p1, p2)
            result += cost
        
        return result
    
    def find(self, node):
        if self.root[node] == node: return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]: self.root[root1] = self.root[root2]
            else: self.root[root2] = self.root[root1]
    
    def connected(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        return root1 == root2

solution = Solution()
print(solution.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(solution.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]]))
print(solution.minCostConnectPoints(points = [[1,2], [3,4]]))