from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2, result = set(nums1), set(nums2), set()
        for num in nums1:
            if num in nums2: result.add(num)
        return list(result)


class Solution:
    """Binary Search WTFF"""
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        res = []
        nums1 = sorted(nums1)
        nums2 = set(nums2)
        for i in nums2:
            l,r = 0,len(nums1)-1
            while l <=r:
                m = (l+r)>>1
                if nums1[m] == i:
                    res.append(i)
                    break
                else:
                    if nums1[m] < i:
                        l = m + 1
                    else:
                        r = m - 1
        return res