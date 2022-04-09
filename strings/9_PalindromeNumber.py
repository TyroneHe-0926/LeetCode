class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strx = str(x)
        start = 0
        end = len(strx)-1
        while start != end:
            if strx[start] != strx[end]:
                return False
            if end ==  start + 1:
                return strx[start] == strx[end]
            start += 1
            end -= 1
        return True
        

if __name__ == "__main__":
    solution = Solution()
    x = 1221
    print(solution.isPalindrome(x))
    x = -121
    print(solution.isPalindrome(x))
    x = 10
    print(solution.isPalindrome(x))