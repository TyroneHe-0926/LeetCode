from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        results = []
        if not nums:
            if upper == lower:
                return [str(upper)]
            else:
                result = f"{lower}->{upper}"
                results.append(result)
                return results
            
        length = len(nums) - 1

        if lower != nums[0]:
            if abs(nums[0] - lower) == 1:
                results.append(str(lower))
            else:
                result = f"{lower}->{nums[0]-1}"
                results.append(result)
        
        for index, number in enumerate(nums):
            if index+1 < len(nums) and nums[index+1] - number != 1:
                diff = abs(nums[index+1] - number)
                if diff == 2:
                    results.append(str(nums[index+1]-1))
                else:
                    result = f"{number+1}->{number+diff-1}"
                    results.append(result)
        
        if upper != nums[length]:
            if abs(upper - nums[length] == 1):
                results.append(str(upper))
            else:
                result = f"{nums[length]+1}->{upper}"
                results.append(result)
        return results

solution = Solution()
nums, lower, upper = [0,1,3,50,75], 0, 99
print(solution.findMissingRanges(nums, lower, upper))
nums, lower, upper = [-1], -2, -1
print(solution.findMissingRanges(nums, lower, upper))