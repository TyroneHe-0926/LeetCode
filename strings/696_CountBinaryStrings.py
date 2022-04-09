from itertools import groupby

class Solution:
    """
    group into 0s and 1s, 
    take the min length bewteen cur group and next group in groups
    """
    def countBinarySubstrings(self, s: str) -> int:
        groups, count = ["".join(group) for _, group in groupby(s)], 0
        for index, group in enumerate(groups):
            if index+1 <= len(groups) - 1:
                count += min(len(group), len(groups[index+1]))
        return count

"""
Leetcode O(n) Space
class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in xrange(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
"""

solution = Solution()
s = "00110011"
print(solution.countBinarySubstrings(s))
s = "001101"
print(solution.countBinarySubstrings(s))