from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums: return ranges
        lower = cur = nums[0]
        for num in nums[1:]:
            if num == cur+1: 
                cur = num
                continue
            ranges.append(f'{lower}->{cur}') if lower != cur else ranges.append(str(cur))
            lower = cur = num
        ranges.append(f'{lower}->{cur}') if lower != cur else ranges.append(str(cur))
        return ranges

solution = Solution()
print(solution.summaryRanges(nums = [0,1,2,4,5,7]))
print(solution.summaryRanges(nums = [0,2,3,4,6,8,9]))
print(solution.summaryRanges(nums = [1,2,3,4,5,6]))