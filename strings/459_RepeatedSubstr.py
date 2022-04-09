class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lps, plen, i, j = [0], len(s), 1, 0
        while i < plen:
            if s[i] == s[j]:
                j+=1
                lps.append(j)
                i+=1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
                    lps.append(0)
        return lps[plen-1] and not plen % (plen-(lps[plen-1]))

class Solution2:
    """
    I liked this solution and would like to explain this in a simple way.

    ss = (s + s)[1:-1]
    return ss.find(s) != -1

    The maximum length of a "repeated" substring that you could get from a string would be half it's length
    For example, s = "abcdabcd", "abcd" of len = 4, is the repeated substring.
    You cannot have a substring >(len(s)/2), that can be repeated.

    So, when ss = s + s , we will have atleast 4 parts of "repeated substring" in ss.
    (s+s)[1:-1], With this we are removing 1st char and last char => Out of 4 parts of repeated substring, 2 part will be gone (they will no longer have the same substring).
    ss.find(s) != -1, But still we have 2 parts out of which we can make s. And that's how ss should have s, if s has repeated substring.
    """
    def repeatedSubstringPattern(self, str):
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        return ss.find(str) != -1

solution = Solution()
print(solution.repeatedSubstringPattern(s = "bb"))
print(solution.repeatedSubstringPattern(s = "abab"))
print(solution.repeatedSubstringPattern(s = "aba"))
print(solution.repeatedSubstringPattern(s = "abcdabcabcabc"))