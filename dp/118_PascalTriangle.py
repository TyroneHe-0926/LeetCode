from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        values = []
        def gen(numRow):
            if numRow == 1:
                values.append([1])
                return [1]
            if numRow == 2:
                values.append([1])
                values.append([1,1])
                return [1,1]
            result = gen(numRow-1)
            value = [1] + [result[i] + result[i+1] for i in range(len(result)) if i < len(result)-1] + [1]
            values.append(value)
            return value
        gen(numRows)
        return values

"""Iterative Solution Leetcode O(numRow2)"""
class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        l=[0]*numRows
        for i in range(numRows):
            l[i]=[0]*(i+1)
            l[i][0]=1
            l[i][i]=1
            for j in range(1,i):
                l[i][j]=l[i-1][j-1]+l[i-1][j]
        return l

solution = Solution()
print(solution.generate(500))
solution2 = Solution()
print(solution2.generate(500))