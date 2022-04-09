class Solution:
    def longestPrefix(self, s: str) -> str:
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
                    lps.append(0)
                    i += 1
        maxm, maxmi = lps[-1], len(lps)-1
        return "".join(s[maxmi-maxm+1:maxmi+1])

solution = Solution()
print(solution.longestPrefix(s = "level"))
print(solution.longestPrefix(s = "ababab"))
print(solution.longestPrefix(s = "bba"))

class Solution2:
    """Leetcode rolling hash solution"""
    def longestPrefix(self, s):
        # res stores the index of the end of the prefix, used for output the result
        # l stores the hash key for prefix
        # r stores the hash key for suffix
        # mod is used to make sure that the hash value doesn't get too big, you can choose another mod value if you want.
        res, l, r, mod = 0, 0, 0, 10**9 + 7

        # now we start from the beginning and the end of the string
        # note you shouldn't search the whole string! because the longest prefix and suffix is the string itself
        for i in range(len(s) - 1):

            # based on an idea that is similar to prefix sum, we calculate the prefix hash in O(1) time.
            # specifically, we multiply the current prefix by 128 (which is the length of ASCII, but you can use another value as well)
            # then add in the ASCII value of the upcoming letter
            l = (l * 128 + ord(s[i])) % mod

            # similarly, we can calculate the suffix hash in O(1) time.
            # Specifically, we get the ith letter from the end using s[~i], note ~i is -i-1
            # we find the pow(128, i, mod) and multiply by the letter's ASCII value
            # Actually, if we don't care about the beautifulness of the code, you can have a variable to keep track of pow(128, i, mod) as you increase i
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod

            # we check if the prefix and suffix agrees, if yes, we find yet another longer prefix, so we record the index
            if l == r: res = i + 1

        # after we finish searching the string, output the prefix
        return s[:res]