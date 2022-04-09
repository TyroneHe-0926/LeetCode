from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nmap = defaultdict(bool)
        for num in nums:
            if nmap[num]: return True
            nmap[num] = True
        return False