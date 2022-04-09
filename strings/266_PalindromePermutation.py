from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cmap, odd = defaultdict(int), 0
        for char in s:
            cmap[char] += 1
        for char in cmap:
            if cmap[char]%2: odd+=1
        return not odd > 1

solution = Solution()
print(solution.canPermutePalindrome(s = "carerac"))
print(solution.canPermutePalindrome(s = "aab"))
print(solution.canPermutePalindrome(s = "aabbddeeecccff"))