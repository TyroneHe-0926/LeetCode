from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zeros = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0: 
                nums.pop(i)
                zeros += 1
        nums += [0] * zeros

"""
LC c++ swaping in place min operations
void moveZeroes(vector<int>& nums) {
    for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        if (nums[cur] != 0) {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }
}
"""