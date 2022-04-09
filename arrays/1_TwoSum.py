from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = defaultdict(list)
        for index, number in enumerate(nums):
            nmap[number].append(index)

        for index, number in enumerate(nums):
            cur_target = target - number
            if nmap[cur_target]:
                if cur_target == number and len(nmap[cur_target]) > 1:
                    return [index, nmap[cur_target][1]]
                elif cur_target != number:
                    return [index, nmap[cur_target][0]]

class Solution:
    """One pass"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = defaultdict(int)
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nmap:
                return [index, nmap[complement]]
            nmap[num] = index


if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums, target))
    nums = [3,2,4]
    target = 6
    print(solution.twoSum(nums, target))
    nums = [3,3]
    target = 6
    print(solution.twoSum(nums, target))