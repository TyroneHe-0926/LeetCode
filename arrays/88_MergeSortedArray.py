from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[:] = nums1[0:m]
        nums1 += nums2
        nums1.sort()
        
solution = Solution()
nums1 = [-1,0,0,3,3,3,0,0,0]
m = 6
nums2 = [1,2,2]
n = 3
solution.merge(nums1, m, nums2, n)
print(nums1)