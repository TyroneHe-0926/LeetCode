from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites: return True
        self.finish = True
        self.memo = defaultdict(bool)
        graph, courses = defaultdict(list), set()
        for preq, course in prerequisites:
            graph[course].append(preq)
            courses.add(course)

        for course in courses:
            self.dfs(course, [], graph)

        return self.finish
        
    def dfs(self, node, seen: List, graph:defaultdict):
        if node in self.memo: return self.memo[node]
        if self.finish:
            if node in seen:
                self.finish = False
                return False
            seen.append(node)
            for n in graph[node]:
                self.memo[n] = self.dfs(n, seen, graph)
                if seen: seen.pop()
            return True
        else: return False

solution = Solution()
print(solution.canFinish(numCourses = 3, prerequisites = [[1,0],[2,0],[0,2]]))
print(solution.canFinish(numCourses = 20, prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
print(solution.canFinish(numCourses = 7, prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))