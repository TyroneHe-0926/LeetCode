class LCSolution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

class MySolution:
    def validPalindrome(self, s: str) -> bool:
        start, end, removed = 0, len(s)-1, False
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                start_removed, end_removed = s[:start] + s[start+1:], s[:end] + s[end+1:]
                if self.checkPalindrome(start_removed) and not removed:
                    removed = True
                    start += 1
                elif self.checkPalindrome(end_removed) and not removed:
                    removed = True
                    end -= 1
                else:
                    return False
        return True
    
    def checkPalindrome(self, s: str):
        start, end = 0, len(s)-1
        if len(s) == 2:
            return s[0] == s[1]
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

s = MySolution()
print(s.validPalindrome(s = "abc"))
print(s.validPalindrome(s = "debbe"))