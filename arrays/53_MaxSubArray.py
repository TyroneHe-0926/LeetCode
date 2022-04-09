from typing import List
import math

class KadaneSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = nums[0]
        for i in range(1, len(nums), 1):
            if nums[i - 1] > 0: nums[i] += nums[i - 1]
            max_val = max(max_val, nums[i])
        return max_val

class DivideConquerSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)

solution = KadaneSolution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))
nums = [0]
print(solution.maxSubArray(nums))
nums = [5,4,-1,7,8]
print(solution.maxSubArray(nums))