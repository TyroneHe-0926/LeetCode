from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        ret_str = ""
        for index, char in enumerate(strs[0]):
            for word in strs[1:]:
                if word[index] != char:
                    return ret_str
            ret_str+=char
        return ret_str

solution = Solution()
strs = ["flower","flow","flight"]
print(solution.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(solution.longestCommonPrefix(strs))