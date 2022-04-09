from typing import List
from collections import Counter, defaultdict

class Solution:
    #DP table approach with sliding window, check leetcode video if forgot
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        dp = defaultdict(int)
        result = 0

        for index in range(len(nums)-1):
            cur_window = nums[index:index+3]
            if self.check_diff(cur_window) and len(cur_window) == 3:
                dp[index+2] = dp[index+1]+1
        
        for item in dp:
            result += dp[item]
        
        return result


    def check_diff(self, t):
        diff = Counter([t[i+1]-t[i] for i in range(len(t)-1)])
        return len(diff) == 1


solution = Solution()
nums = [1,2,3,4]
print(solution.numberOfArithmeticSlices(nums))
nums = [1,3,5,7,9]
print(solution.numberOfArithmeticSlices(nums))
nums = [7,7,7,7]
print(solution.numberOfArithmeticSlices(nums))
nums = [1,2,3,8,9,10]
print(solution.numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6]
print(solution.numberOfArithmeticSlices(nums))
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(solution.numberOfArithmeticSlices(nums))