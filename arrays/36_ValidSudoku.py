from typing import List

class Solution:
    indexes = {0: 0,1: 3,2: 6}
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [j for j in board[i] if j != '.']
            col = [board[j][i] for j in range(9) if board[j][i] != '.']
            r,c = self.indexes[i//3], self.indexes[i%3]
            box = [board[r+j][c+k] for k in range(3) for j in range(3) if board[r+j][c+k] != '.']
            if not (len(row) == len(set(row)) and len(col) == len(set(col)) and len(box) == len(set(box))): return False
        return True

class HashSetSolution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # Use hash set to record the status
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                # Check if the position is filled with number
                if val == ".":
                    continue

                # Check the row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check the column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check the box
                idx = (r // 3) * 3 + c // 3
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)

        return True

"""
Leetcode bitmask check question
"""
solution = Solution()
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))