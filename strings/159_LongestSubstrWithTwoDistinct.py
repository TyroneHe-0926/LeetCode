from collections import defaultdict

class Solution: #kinda like the longest substr without repeat, except we keeping the map of 2
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        smap = defaultdict(int)
        result = ""
        ret_result = 0
        for index, char in enumerate(s):
            if len(smap) == 2 and char not in smap:
                furthest = min(smap, key=smap.get)
                del smap[furthest]
                result = result[result.rindex(furthest)+1:]

            smap[char] = index
            result += char
            if len(result) > ret_result:
                ret_result = len(result)
        
        return ret_result


solution = Solution()
s = "cdaba"
print(solution.lengthOfLongestSubstringTwoDistinct(s))