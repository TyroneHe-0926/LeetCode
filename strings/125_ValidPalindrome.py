class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if s[start].lower() == s[end].lower():
                start += 1
                end -= 1
            elif not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                return False
        return True

s = Solution()
print(s.isPalindrome(s = "A man, a plan, a canal: Panama"))
print(s.isPalindrome(s = "race a car"))
print(s.isPalindrome(s = "0P"))