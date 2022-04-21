class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        slen = len(s)
        zigzags = [[' ' for _ in range(slen)] for _ in range(slen )] 
        sindex = zrow = zcol = 0
        while sindex < slen:
            if zcol == numRows - 1:
                zigzags[zcol][zrow] = s[sindex]
                while zcol > 0:
                    zcol -= 1
                    zrow += 1
                    sindex += 1
                    zigzags[zcol][zrow] = s[sindex] if sindex < slen else ' '
            else:
                zigzags[zcol][zrow] = s[sindex]
                sindex += 1
                zcol += 1

        result = ""
        for row in zigzags:
            for col in row:
                if col != ' ': result += col
        
        return result

solution = Solution()
print(solution.convert(s = "PAYPALISHIRING", numRows = 3))
print(solution.convert(s = "PAYPALISHIRING", numRows = 4))
print(solution.convert(s = "ABCD", numRows = 2))