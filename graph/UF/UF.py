class QuickFindGraph:

    def __init__(self, length):
        self.root = [i for i in range(length)]
    
    def find(self, vertex):
        return self.root[vertex]
    
    def union(self, vertex1, vertex2):
        v1 = self.find(vertex1)
        v2 = self.find(vertex2)
        if v1 != v2:
            for index, _ in enumerate(self.root):
                if self.root[index] == v2:
                    self.root[index] = v1
    
    def connected(self, vertex1, vertex2):
        return self.find(vertex1) == self.find(vertex2)

class QuickUnionGraph:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class OptiomizedQuickUnionGraph:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        # Use a rank array to record the height of each vertex, i.e., the "rank" of each vertex.
        # The initial "rank" of each vertex is 1, because each of them is
        # a standalone vertex with no connection to other vertices.
        self.rank = [1] * size

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

    def connected(self, x, y):
        return self.find(x) == self.find(y)

def testQFG():
    uf = QuickFindGraph(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true

def testQUG():
    uf = QuickUnionGraph(5)

    uf.union(1, 0)
    uf.union(2, 0)
    uf.union(3, 0)
    uf.union(4, 0)
    print(uf.root)

def testOptimized():
    uf = OptiomizedQuickUnionGraph(5)
    print(uf.root)
    uf.union(1, 0)
    uf.union(2, 0)
    uf.union(3, 0)
    uf.union(4, 0)
    print(uf.root)

if __name__ == "__main__":
    testQUG()
    testOptimized()