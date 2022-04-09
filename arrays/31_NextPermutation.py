from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, -1, -1):
            if i-1 > -1 and nums[i-1] < nums[i]:
                replacement = i+self.find_smallest_bigger(nums[i:], nums[i-1])
                nums[i-1], nums[replacement] = nums[replacement], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums[:] = nums[::-1]
        
    def find_smallest_bigger(self, arr, target):
        maxi, maxm = 0, 101
        for index, num in enumerate(arr):
            if num > target and maxm > num:
                maxm, maxi = num, index
        return maxi

solution = Solution()
nums = [1,2,3]
solution.nextPermutation(nums)
print(nums)
nums2 = [3,2,1]
solution.nextPermutation(nums2)
print(nums2)
nums3 = [1,1,5]
solution.nextPermutation(nums3)
print(nums3)