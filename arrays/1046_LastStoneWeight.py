from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            first, second = stones[-1], stones[-2]
            if first == second: del stones[-2:]
            else:
                diff = first - second
                del stones[-2:]
                stones.insert(self.index(diff, stones), diff)
                    
        return 0 if not stones else stones[0]
    
    def index(self, target, arr):
        left,mid,right = 0, 0, len(arr)-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] > target:
                right = mid-1
            elif arr[mid] < target:
                left = mid + 1
            else:
                return mid+1
        return left 


class Solution:
    """heap"""
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Make all the stones negative. We want to do this *in place*, to keep the
        # space complexity of this algorithm at O(1). :-)
        for i in range(len(stones)):
            stones[i] *= -1

        # Heapify all the stones.
        heapq.heapify(stones)

        # While there is more than one stone left, remove the two
        # largest, smash them together, and insert the result
        # back into the heap if it is non-zero.
        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones, stone_1 - stone_2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0
    
solution = Solution()
print(solution.lastStoneWeight(stones = [2,7,4,1,8,1]))
print(solution.lastStoneWeight(stones = [1,1,2,2,3,3]))