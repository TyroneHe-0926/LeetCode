from typing import List
from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nmap, hit = defaultdict(int), 0

        for num in nums:
            comp = k - num
            if comp in nmap and nmap[comp] != 0:
                hit += 1
                nmap[comp] -= 1
            else:
                nmap[num] += 1
        
        return hit
            

solution = Solution()
print(solution.maxOperations(nums = [1,2,3,4], k = 5))
print(solution.maxOperations(nums = [3,1,3,4,3], k = 6))
print(solution.maxOperations(nums = [1,1,1,1,1,1,1], k = 2))