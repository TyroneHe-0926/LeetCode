from typing import List
from collections import defaultdict

class SolutionBF:
    """O(n3) cuz O(n2) for coming up with all subarr, O(n) for sum, so TLE"""
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums), 1):
                if sum(nums[i:j+1]) == k: count+=1
        return count

class SolutionBFPrefixSum():
    """O(n2) but still TLE for python, O(n) sum O(n) going over the nums array"""
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, count = [], 0
        for index, num in enumerate(nums):
            cursum = [num]
            if num == k: count += 1
            if prefix_sum:
                for psum in prefix_sum:
                    if psum + num == k: count+=1
                    cursum.append(psum + num)
            prefix_sum = cursum
        return count

class Solution():
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqmap, count, cursum = defaultdict(int), 0, 0
        freqmap[0] = 1
        for num in nums:
            cursum += num
            if freqmap[cursum - k]: count += freqmap[cursum-k]
            freqmap[cursum] += 1
        return count

solution = Solution()
print(solution.subarraySum(nums = [1,1,1], k = 2))
print(solution.subarraySum(nums = [1,2,3], k = 3))
print(solution.subarraySum(nums = [1,6,2,1,4,3], k = 7))
print(solution.subarraySum(nums = [1,6,2,-1,-1,3], k = 7))
print(solution.subarraySum(nums = [1], k = 0))
print(solution.subarraySum(nums = [3,4,-3,3,4], k = 7))