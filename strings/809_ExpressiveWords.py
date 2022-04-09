from typing import List
from itertools import groupby

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        """
        split original string into groups
        eg. hello -> ["h", "e", "ll", "o"]

        Apply this same grouping to every query string, and then compare each group
        """

        def group_comp(src_group: List[str], target_group: List[str]):
            """Check if there are chars from og string missing"""
            if len(src_group) != len(target_group):
                return False
            
            for index, group in enumerate(src_group):
                if group != target_group[index]:
                    #if the og group len < 2, meaning we cannot expanding the query group to that
                    if len(target_group[index]) <= 2:
                        return False
                    #different chars
                    elif group[0] != target_group[index][0]:
                        return False
                    #the length of query str group shouldn't be longer than the og one
                    elif len(group) > len(target_group[index]):
                        return False
            
            return True
        
        count = 0
        og_groups = ["".join(group) for _, group in groupby(s)]
        for word in words:
            group = ["".join(group) for _, group in groupby(word)]
            if group_comp(group, og_groups):
                count += 1
        
        return count


solution = Solution()
s = ""
words = ["hello", "hi", "helo"]
print(solution.expressiveWords(s, words))
s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
print(solution.expressiveWords(s, words))