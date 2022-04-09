class Solution:
    def findCircleNum(self, isConnected) -> int:
        #using the optimized graph with path compression and rank
        self.root = [i for i in range(len(isConnected))]
        self.rank = [1] * len(isConnected)
        self.unique_province = []

        #connect the cities first using union
        for current_city, city in enumerate(isConnected):
            for connect_city, connected in enumerate(city):
                if connected == 1:
                    # print(f"connecting {current_city} with {connect_city}")
                    self.union(current_city, connect_city)
        
        # after connecting all the cities, i ll traverse through the root now
        # and find each of the vertext's head using find
        # the return value will be the amount of unique heads, representing a unique province
        for vertex in self.root:
            head = self.find(vertex)
            if head not in self.unique_province:
                self.unique_province.append(head)
        
        return len(self.unique_province)

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

if __name__ == "__main__":
    solution = Solution()
    isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
    print(solution.findCircleNum(isConnected))
    print(solution.root)