from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]


solution = Solution()
nums,k = [3,2,1,5,6,4], 2
print(solution.findKthLargest(nums,k))
nums, k = [3,2,3,1,2,4,5,5,6], 4
print(solution.findKthLargest(nums,k))

"""
class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    [3,2,1,5,6,4], k = 2
    1: heap = [3]
    2: heap = [2,3]
    3: heap = [1,2,3], but k=2 so pop smallest, heap = [2,3]
    4: heap = [2,3,5], but k=2 so pop smallest, heap = [3,5]
    5: heap = [3,5,6], but k=2 so pop smallest, heap = [5,6]
    6: heap = [4,5,6], but k=2 so pop smallest, heap = [5,6]
    7: return heap[0] which is 5
"""

#quick select
class Solution2:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)