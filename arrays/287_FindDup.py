from typing import List

class Solution:
    """Cant believe i came up with this shit"""

    """Treat each number in the list as the target bit to set"""
    """If the target bit is already 1, we have a dup"""
    """
    Tbh this is the first approach i had in mind with the space restriction, 
    plus the no manipulation to the original array thing, 
    I thought I cant modify the original array at all, (no sorting, swapping), well. 
    """

    """
    The lc bit manipulation solution def performs better both space and time wise, 
    since I might be dealing with some crazy large bits here,
    but I felt like it overcomplicated stuff too much, 
    like during a 40 min interview with 2 questions, no way I coulda come up with that I aint no jeff dean
    """

    def findDuplicate(self, nums: List[int]) -> int:
        temp = 0
        for num in nums:
            if self.check_bit(temp, num): return num
            temp = self.set_bit(temp, num)
    
    def set_bit(self, value, bit):
        return value | (1<<bit)
    
    def check_bit(self, value, bit):
        return (1 << bit) & value

class SolutionBinarySearch:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate

class SolutionFloyd:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tortoise = nums[0]

        while True:
            tortoise, hare = nums[tortoise], nums[nums[hare]]
            if tortoise == hare: break
        
        tortoise = nums[0]

        while tortoise != hare:
            tortoise, hare = nums[tortoise], nums[hare]
                
        return hare

solution = SolutionFloyd()
print(solution.findDuplicate(nums = [1,3,4,2,2]))
print(solution.findDuplicate(nums = [3,1,3,4,2]))
print(solution.findDuplicate(nums = [2,5,9,6,9,3,8,9,7,1]))