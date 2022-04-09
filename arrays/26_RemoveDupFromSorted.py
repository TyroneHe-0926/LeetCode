from typing import List
from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return []
        cur = nums[0]
        for index, number in enumerate(nums[1:]):
            if number == cur:
                nums[index] = "_"
            elif number != cur:
                cur = number
        
        nums[:] = (i for i in nums if i != "_")

nums1 = [0,0,1,1,1,2,2,3,3,4]
nums2 = [1,1,2]
solution = Solution()
solution.removeDuplicates(nums1)
print(nums1)
solution.removeDuplicates(nums2)
print(nums2)


"""
nmap = defaultdict(int)
for number in nums:
    nmap[number] += 1
nums[:] = [i for i in nmap]
"""