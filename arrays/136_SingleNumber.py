from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nmap = defaultdict(int)
        for num in nums:
            nmap[num] += 1
        
        for num in nmap:
            if nmap[num] == 1: return num

class Solution:
    def singleNumber(self, nums):
        """2 * (a+b+c) - (a+a+b+b+c)=c"""
        return 2 * sum(set(nums)) - sum(nums)

class Solution:
    def singleNumber(self, nums):
        """
        If we take XOR of zero and some bit, it will return that bit
        a XOR 0 = a
        If we take XOR of two same bits, it will return 0
        a XOR a = 0
        a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b
        So we can XOR all bits together to find the unique number.
        """
        a = 0
        for i in nums:
            a ^= i
        return a