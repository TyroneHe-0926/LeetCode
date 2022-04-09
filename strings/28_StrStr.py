class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1
        lps = self.lps_build(pattern=needle)
        return self.kmp(s=haystack, pattern=needle, lps=lps)
    
    def lps_build(self, pattern):
        lps, plen, i, j = [0], len(pattern), 1, 0
        while i < plen:
            if pattern[i] == pattern[j]:
                j+=1
                lps.append(j)
                i+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    lps.append(0)
                    i+=1
        return lps

    def kmp(self, s, pattern, lps):
        slen, plen, i, j = len(s), len(pattern), 0, 0
        while i < slen:
            if s[i] == pattern[j]:
                i+=1
                j+=1
            if j == plen:
                return i-j
                # j = lps[j-1]
            elif i < slen and s[i] != pattern[j]:
                if j != 0:
                    j = lps[j-1]
                else:
                    i+=1
        return -1

solution = Solution()
print(solution.strStr(haystack = "a", needle = "a"))
# print(solution.lps_build("ABCDE"))
# print(solution.lps_build("AAAA"))