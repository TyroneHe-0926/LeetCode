class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha(): return len(s[i])