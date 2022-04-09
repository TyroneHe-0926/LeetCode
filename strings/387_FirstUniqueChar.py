from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charmap, bad = defaultdict(int), set()
        for index, char in enumerate(s):
            if char in charmap: 
                bad.add(char)
                del charmap[char]
            elif char not in charmap and char not in bad: charmap[char] = index
        return -1 if not charmap else charmap[next(iter(charmap))]
    
solution = Solution()
s = "leetcode"
print(solution.firstUniqChar(s))
s = "loveleetcode"
print(solution.firstUniqChar(s))
s = "aabb"
print(solution.firstUniqChar(s))