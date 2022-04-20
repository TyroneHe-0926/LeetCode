from functools import lru_cache
"""Crazy LC memoization solution"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            
            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(text1) or p2 == len(text2):
                return 0
            
            # Recursive case 1.
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            
            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
            
        return memo_solve(0, 0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Create the boundry and initialize all to 0 so we dont have to do
        All the boundry checks while looping, and its more elegant
        """
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for row, tc1 in enumerate(text1):
            for col, tc2 in enumerate(text2):
                if tc2 == tc1: dp[col+1][row+1] = dp[col][row]+1
                else: dp[col+1][row+1] = max(dp[col][row+1], dp[col+1][row])
        return dp[-1][-1]
                    
solution = Solution()
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
print(solution.longestCommonSubsequence(text1 = "abc", text2 = "def"))
print(solution.longestCommonSubsequence(text1 = "dododadabohahafhahabobabahahafhaha", text2 = "dodoabahaabahahafhahabqibvqqsad"))