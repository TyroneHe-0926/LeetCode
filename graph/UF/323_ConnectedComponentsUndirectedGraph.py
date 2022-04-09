class Solution:
    def countComponents(self, n, edges) -> int:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.unique = []

        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            self.union(node1, node2)
        
        for node in self.root:
            head = self.find(node)
            if head not in self.unique:
                self.unique.append(head)
        
        return len(self.unique)
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.root[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.root[root1] = root2
            else:
                self.root[root2] = root1
                self.rank[root1] += 1

    def find(self, node):
        if self.root[node] == node:
            return self.root[node]
        
        self.root[node] = self.find(self.root[node])
        return self.root[node]

if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [[0,1],[1,2],[3,4]]
    edges2 = [[0,1],[1,2],[2,3],[3,4]]
    print(solution.countComponents(n, edges))
    print(solution.countComponents(n, edges2))