from typing import List
from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites: return [i for i in range(numCourses-1, -1, -1)]
        self.finish = True
        self.visited = set()
        self.memo = defaultdict(bool)
        graph, courses = defaultdict(list), set()
        for preq, course in prerequisites:
            graph[course].append(preq)
            courses.add(course)

        self.paths = []
        for course in courses:
            if course not in self.visited: self.dfs(course, [], graph)
            if not self.finish: return []

        for i in range(numCourses):
            if i not in self.paths: self.paths.append(i)
        
        return self.paths[::-1]
        
    def dfs(self, node, seen: List, graph:defaultdict):
        if node in self.memo: return self.memo[node]
        if self.finish:
            if node in seen:
                self.finish = False
                return False
            self.visited.add(node)
            seen.append(node)
            for n in graph[node]:
                self.memo[n] = self.dfs(n, seen, graph)
                if seen: seen.pop()
            if node not in self.paths: self.paths.append(node)
            return True
        else: return False

solution = Solution()
print(solution.findOrder(numCourses = 3, prerequisites = [[1,0],[2,0],[0,2]]))
print(solution.findOrder(numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
print(solution.findOrder(numCourses = 7, prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))