class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result = []
        results = []
        for c in s:
            if c in result:
                for index, char in enumerate(result):
                    if char == c:
                        result = result[index+1:]
                        result.append(c)
                        break
            else:
                result.append(c)
                results.append(len(result))
        
        return max(results)

class SolutionRework:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        result, maxm = [], 0
        for c in s:
            if c in result:
                result = result[result.index(c)+1:]
                result.append(c)
            else:
                result.append(c)
                if len(result) > maxm: maxm = len(result)
        return maxm
    

if __name__ == "__main__":
    solution = Solution()
    # s = "abcabcbb"
    # solution.lengthOfLongestSubstring(s)
    # s = "a"
    # solution.lengthOfLongestSubstring(s)
    # s = "pwwkew"
    # solution.lengthOfLongestSubstring(s)
    case1 = "aba"
    solution.lengthOfLongestSubstring(case1)
    