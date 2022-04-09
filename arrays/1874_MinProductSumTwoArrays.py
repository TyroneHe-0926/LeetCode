from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2, result = sorted(nums1), sorted(nums2, reverse=True), 0
        for i in range(len(nums1)): result += nums1[i] * nums2[i]
        return result

class Solution:
    """O(n+k) using Counting sort"""
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize counter1 and counter2.
        counter1, counter2 = [0] * 101, [0] * 101

        # Record the number of occurrence of elements in nums1 and nums2.
        for num in nums1:
            counter1[num] += 1
        for num in nums2:
            counter2[num] += 1
        
        # Initialize two pointers p1 = 1, p2 = 100.
        # Stands for counter1[1] and counter2[100], respectively.
        p1, p2 = 1, 100
        ans = 0
        
        # While the two pointers are in the valid range.
        while p1 <= 100 and p2 > 0:

            # If counter1[p1] == 0, meaning there is no element equals p1 in counter1,
            # thus we shall increment p1 by 1.
            while p1 <= 100 and counter1[p1] == 0:
                p1 += 1

            # If counter2[p2] == 0, meaning there is no element equals p2 in counter2,
            # thus we shall decrement p2 by 1.
            while p2 > 0 and counter2[p2] == 0:
                p2 -= 1

            # If any of the pointer goes beyond the border, we have finished the 
            # iteration, break the loop.
            if p1 == 101 or p2 == 0:
                break

            # Otherwise, we can make at most min(counter1[p1], counter2[p2]) 
            # pairs {p1, p2} from nums1 and nums2, let's call it occ. 
            # Each pair has product of p1 * p2, thus the cumulative sum is 
            # incresed by occ * p1 * p2. Update counter1[p1] and counter2[p2].
            occ = min(counter1[p1], counter2[p2])
            ans += occ * p1 * p2
            counter1[p1] -= occ
            counter2[p2] -= occ
        
        # Once we finish the loop, return ans as the product sum.
        return ans       

solution = Solution()
print(solution.minProductSum(nums1 = [5,3,4,2], nums2 = [4,2,2,5]))
print(solution.minProductSum(nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]))