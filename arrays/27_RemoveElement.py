from typing import List

#two pointers with space O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        for index, num in enumerate(nums):
            if num != val:
                nums[start] = nums[index]
                start += 1
        return start

solution = Solution()
l, k = [0,1,2,2,3,0,4,2], 2
solution.removeElement(l, k)
print(l)