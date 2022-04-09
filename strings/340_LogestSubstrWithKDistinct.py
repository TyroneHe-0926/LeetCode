from collections import defaultdict

class Solution: #just took my with 2 code and changed it to K lol
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        smap = defaultdict(int)
        result = ""
        ret_result = 0
        if not k:
            return ret_result
        for index, char in enumerate(s):
            if len(smap) == k and char not in smap:
                furthest = min(smap, key=smap.get)
                del smap[furthest]
                result = result[result.rindex(furthest)+1:]

            smap[char] = index
            result += char
            if len(result) > ret_result:
                ret_result = len(result)
        
        return ret_result