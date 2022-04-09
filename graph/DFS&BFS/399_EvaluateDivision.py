from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:  
        def dfs(start, end, visited):
            if start == end:
                return 1.0
                
            visited.add(start)

            for node in m[start]:
                if node not in visited:
                    division = dfs(node, end, visited)
                    if(division > 0):
                        return division * m[start][node]
            
            return -1  
        
        m = defaultdict(dict)

        for (x,y), (value) in zip(equations, values):
            m[x][y] = value
            m[y][x] = 1.0/value
        
        print(m)

        ans = [-1.0 if not m[div1] or not m[div2] else dfs(div1, div2, set()) for (div1, div2) in queries]
        
        return ans


if __name__ == "__main__":
    solution = Solution()
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x2","x4"]]
    print(solution.calcEquation(equations, values, queries))