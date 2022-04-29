from collections import defaultdict

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cmap, alphabet, result = defaultdict(int), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 0
        for i, c in enumerate(alphabet): cmap[c] = i+1
        cur = 0
        for i in range(len(columnTitle)-1, -1, -1):
            result += (cmap[columnTitle[i]]) * (26 ** cur)
            cur += 1
        return result

solution = Solution()
print(solution.titleToNumber('AAB'))