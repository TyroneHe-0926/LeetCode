from typing import List
from collections import defaultdict

class Solution: 
    """
    sorted sring hashmap O(NKlogK) Runtime where N is the length of strs, and K is the maximum length of a string in strs
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list)
        for string in strs:
            amap["".join(sorted(string))].append(string)
        return [amap[group] for group in amap]

class SolutionHashByCount: #O(NK)
    def groupAnagrams(strs):
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

solution = Solution()
print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))