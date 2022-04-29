from typing import List
from collections import defaultdict

class Solution:
    """!--- Didn't even do it, just looked at solution, need to go over again sometimes --!"""
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = defaultdict(int)
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True