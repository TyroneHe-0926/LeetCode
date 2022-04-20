class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        lastnum = 0
        s = s.split(" ")
        for word in s:
            if word.isdecimal() and int(word) <= lastnum: return False
            elif word.isdecimal(): lastnum = int(word)
        return True
