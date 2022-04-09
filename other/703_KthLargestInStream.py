from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.kth = k

    def add(self, val: int) -> int:
        index = self.insert(val)
        self.nums.insert(index, val)
        return self.nums[-self.kth]

    def insert(self, val: int):
        left,mid,right = 0,0,len(self.nums)-1
        while left <= right:
            mid = (left+right)//2
            if self.nums[mid] > val:
                right = mid - 1
            elif self.nums[mid] < val:
                left = mid + 1
            else:
                return mid
        return left


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))