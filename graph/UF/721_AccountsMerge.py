from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.root = [i for i in range(len(accounts))]
        self.rank = [1] * len(accounts)
        self.usermap = defaultdict(list)
        self.seen = defaultdict(int)

        merged = defaultdict(list)

        for index, users in enumerate(accounts):
            emails = users[1:]
            for email in emails: 
                for index2, search in enumerate(accounts[index+1:]):
                    if email in search[1:]:
                        self.union(index, index+index2+1)
                        break
                if email not in self.seen:
                    self.usermap[index].append(email)
                    self.seen[email] = index
        
        for index, node in enumerate(self.root):
            mergenode = self.find(node)
            for useremail in self.usermap[index]:
                if useremail not in merged[mergenode]:
                    merged[mergenode].append(useremail)
            merged[mergenode].sort()

        result = []
        for item in merged:
            user = accounts[item][0]
            result.append([user]+merged[item])
        return result

    def find(self, node):
        if self.root[node] == node:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 != root2:
            if self.rank[root2] > self.rank[root1]:
                self.root[root1] = self.root[root2]
                self.rank[root2] += 1
            else:
                self.root[root2] = self.root[root1]
                self.rank[root1] += 1

"""LC solution with 192ms"""
class UF:
    def __init__(self, N):
        self.parents = list(range(N))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
class Solution:
    # 196 ms, 82.09%. 
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        
        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        # Append emails to correct index
        ans = defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)
        
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

solution = Solution()
print(solution.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(solution.accountsMerge(accounts = [["David","David0@m.co","David1@m.co"],["David","David1@m.co","David2@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David3@m.co","David4@m.co"]]))