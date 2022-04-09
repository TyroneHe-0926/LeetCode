from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_index = len(nums) - 1
        last_visited = end_index
        for i in range(end_index, -1, -1):
            if i + nums[i] >= last_visited:
                last_visited = i
        return last_visited == 0


solution = Solution()
nums = [2,1,3,1,4]
print(solution.canJump(nums))
nums = [3,2,1,0,4]
print(solution.canJump(nums))
case1 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(solution.canJump(case1))

"""
TLE with a dp backtrack recusion already
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = []
        bad = []
        
        return self.canJumpHelper(nums, 0, good, bad)
    
    def canJumpHelper(self, nums, index, good, bad):
        if index == len(nums)-1:
            return True
        
        if index in good:
            return True
        elif index in bad:
            return False
        
        jump_index = nums[index]
        for i in range(index+1, index+jump_index+1, 1):
            if self.canJumpHelper(nums, i, good, bad):
                return True
            else:
                bad.append(i)

        return False
"""