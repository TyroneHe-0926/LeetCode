from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.search(nums = [-1,0,3,5,9,12], target = 9))
    print(solution.search(nums = [-1,0,3,5,9,12], target = 2))