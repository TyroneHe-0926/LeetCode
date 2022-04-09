class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s2 = s
        t2 = t
        for index, char in enumerate(s):
            if char == "#":
                diff = len(s) - len(s2)
                remove_index = index - diff
                if remove_index - 1 > 0:
                    s2 = s2[:remove_index-1]+s2[remove_index+1:]
                else:
                    s2 = s2[remove_index+1:]

        for index, char in enumerate(t):
            if char == "#":
                diff = len(t) - len(t2)
                remove_index = index - diff
                if remove_index - 1 > 0:
                    t2 = t2[:remove_index-1]+t2[remove_index+1:]
                else:
                    t2 = t2[remove_index+1:]
        
        return s2 == t2

solution = Solution()
# s,t = "ab#c","ad#c"
# print(solution.backspaceCompare(s,t))
# s,t = "ab##","c#d#"
# print(solution.backspaceCompare(s,t))
s,t = "a#c", "b"
print(solution.backspaceCompare(s,t))

"""
LC Two pointers solution
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))
"""