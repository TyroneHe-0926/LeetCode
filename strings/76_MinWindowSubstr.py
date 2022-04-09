from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = Counter(t)
        cur_str = ""
        results = []

        for char in s:
            cur_str += char
            while self.check_match(cur_str, tmap):
                results.append(cur_str)
                cur_str = cur_str[1:]
        
        results.sort(key=len)

        return "" if len(results) == 0 else results[0]

    def check_match(self, src_str, tmap):
        counter = Counter(src_str)
        for char in tmap:
            if char in counter:
                if counter[char] < tmap[char]:
                    return False
            else:
                return False
        return True

solution = Solution()
s, t = "ADOBECODEBANC", "ABC"
print(solution.minWindow(s,t))
s, t = "ADOBECADEBANNC", "ABC"
print(solution.minWindow(s,t))
s, t = "a", "a"
print(solution.minWindow(s,t))
s, t = "a", "aa"
print(solution.minWindow(s,t))
s, t = "aa", "aa"
print(solution.minWindow(s,t))