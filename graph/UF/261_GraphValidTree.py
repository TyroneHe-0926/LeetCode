class Solution:
    def validTree(self, n, edges) -> bool:
        # invalid one, there is no one single root node
        # invalid two, trying to connecting something with the same head node 
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.valid = True
        self.unique = []

        for connection in edges:
            node1 = connection[0]
            node2 = connection[1]
            self.union(node1, node2)
            if self.valid:
                continue
            else:
                return self.valid
        
        for vertex in self.root:
            head = self.find(vertex)
            if head not in self.unique:
                self.unique.append(head)

        return len(self.unique) == 1

    # The find function here is the same as that in the disjoint set with path compression.
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    # The union function with union by rank
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
        else:
            self.valid = False

    def connected(self, x, y):
        return self.find(x) == self.find(y)

if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    print(solution.validTree(n, edges))