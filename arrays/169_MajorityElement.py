"""O(n) space and time hashmap"""
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nmap = defaultdict(int)
        half = len(nums)//2
        for num in nums:
            nmap[num] += 1
            if nmap[num] > half: return num

"""Boyer Moore Voting with O(n) time O(1) space"""
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate