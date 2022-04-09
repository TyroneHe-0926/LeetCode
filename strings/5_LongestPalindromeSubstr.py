import time

class Solution():
    def longestPalindrome(self, s: str) -> str:
        n, start, length = len(s), 0, 0
        for i in range(n):
            plen = max(self.get_palindrome(s, i, i),self.get_palindrome(s, i, i+1))
            if plen > length:
                length = plen
                start = i - (plen - 1) // 2
        return s[start : start + length]

    def get_palindrome(self, s, left, right) -> int:
        while left > -1 and right < len(s) and s[left] == s[right]:
            left, right = left-1, right+1
        return right-left-1

class SolutionBruteForce:
    """TLE O(n3)"""
    def longestPalindrome(self, s: str) -> str:
        start = time.time()
        maxm, result = 0, ""
        for i in range(len(s)):
            substr = s[i:]
            for j in range(len(substr)):
                if j+1 > maxm and self.checkPalindrome(substr[0:j+1]):
                    maxm, result = j+1, substr[0:j+1]
        print(time.time() - start)
        return result                

    def checkPalindrome(self, s: str):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]: return False
            start, end = start+1, end-1
        return True

s = Solution()
print(s.longestPalindrome(s = "babad"))
# print(s.longestPalindrome(s = "cbbd"))
# print(s.longestPalindrome(s = "babaaaaaabaaaaaaaaaaaab"))
# print(s.longestPalindrome(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ))