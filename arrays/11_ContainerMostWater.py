from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area = 0, len(height)-1, 0
        while left < right:
            curarea = min(height[left], height[right]) * (right-left)
            area = max(area, curarea)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return area


if __name__ == "__main__":
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    solution.maxArea(height)
    height = [1,1]
    solution.maxArea(height)

    # tcase = [1,2,1]
    # solution.maxArea(tcase)