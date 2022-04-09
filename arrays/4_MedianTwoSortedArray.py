import math
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        half, even, left, right = (total+1)//2, total%2==0, 0, len(nums1)

        while left < right:
            m1 = left + (right-left)//2
            m2 = half - m1
            if nums1[m1] < nums2[m2-1]: left=m1+1
            else: right = m1
        
        m1 = left
        m2 = half-m1

        c1 = max(-math.inf if m1 <= 0 else nums1[m1-1], -math.inf if m2 <= 0 else nums2[m2-1])
        if not even: return c1
        c2 = min(math.inf if m1 > len(nums1)-1 else nums1[m1], math.inf if m2 > len(nums2)-1 else nums2[m2])
        return (c1+c2)/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        total = len(nums1) + len(nums2)
        half, even, left, right = (total)//2, total%2==0, 0, len(nums1) - 1

        while True:
            m1 = (left+right) // 2
            m2 = half - m1 - 2

            n1left, n1right = nums1[m1] if m1 >= 0 else -math.inf, nums1[m1+1] if m1 + 1 < len(nums1) else math.inf
            n2left, n2right = nums2[m2] if m2 >= 0 else -math.inf, nums2[m2+1] if m2 + 1 < len(nums2) else math.inf

            median1, median2 = max(n1left, n2left), min(n1right, n2right)
            if n1left <= n2right and n2left <= n1right:
                if not even: return median2
                return (median1 + median2) / 2
            elif n1left > n2right: right = m1 - 1
            elif n2left > n1right: left = m1 + 1

solution = Solution()
print(solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
print(solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(solution.findMedianSortedArrays(nums1 = [-19,1,2,6,9,24,88], nums2 = [-3,-4,18]))