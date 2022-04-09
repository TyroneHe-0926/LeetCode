class Solution:
    def earliestAcq(self, logs, n) -> int:
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        #just have to fucking sort the logs by time first for it to work .....
        logs.sort(key = lambda x: x[0])

        for log in logs:
            time = log[0]
            node1 = log[1]
            node2 = log[2]
            heads = []

            self.union(node1, node2)
            for node in self.root:
                heads.append(self.find(node))
            
            # print(heads)
            if len(list(set(heads))) == 1:
                return time
        
        return -1

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

if __name__ == "__main__":
    solution = Solution()
    logs1 = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]]
    logs2 = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
    logs3 = [[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]]
    n1 = 4
    n2 = 6
    n3 = 4
    # print(solution.earliestAcq(logs1, n1))
    # print(solution.earliestAcq(logs2, n2))
    print(solution.earliestAcq(logs3, n3))