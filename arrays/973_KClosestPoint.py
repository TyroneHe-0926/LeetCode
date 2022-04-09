import heapq
from typing import List
from collections import defaultdict

class Solution:
    """Simple Heap like the FindKthQuesiton, except this one using max heap"""
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for index, (x, y) in enumerate(points):
            heapq.heappush(pq, (-(x*x+y*y), index))
            if len(pq) > k: heapq.heappop(pq)
        return [points[i[1]] for i in pq]

solution = Solution()
points, k = [[1,3],[-2,2]], 1
print(solution.kClosest(points, k))
points, k = [[3,3],[5,-1],[-2,4]], 2
print(solution.kClosest(points, k))



"""Quick Select"""
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quick_select(points, k)
    
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Perform the QuickSelect algorithm on the list"""
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            # Repeatedly partition the list
            # while narrowing in on the kth element
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        
        # Return the first k elements of the partially sorted list
        return points[:k]
    
    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        """Partition the list around the pivot value"""
        pivot = self.choose_pivot(points, left, right)
        pivot_dist = self.squared_distance(pivot)
        while left < right:
            # Iterate through the range and swap elements to make sure
            # that all points closer than the pivot are to the left
            if self.squared_distance(points[left]) >= pivot_dist:
                points[left], points[right] = points[right], points[left]
                right -= 1
            else:
                left += 1
        
        # Ensure the left pointer is just past the end of
        # the left range then return it as the new pivotIndex
        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left
    
    def choose_pivot(self, points: List[List[int]], left: int, right: int) -> List[int]:
        """Choose a pivot element of the list"""
        return points[left + (right - left) // 2]
    
    def squared_distance(self, point: List[int]) -> int:
        """Calculate and return the squared Euclidean distance."""
        return point[0] ** 2 + point[1] ** 2