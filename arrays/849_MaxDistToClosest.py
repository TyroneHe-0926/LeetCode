from typing import List
from collections import defaultdict
from itertools import groupby

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lmap, rmap = defaultdict(int), defaultdict(int)
        lmap[0], rmap[len(seats)-1] = 0, 0
        for i in range(1,len(seats),1):
            if seats[i] == 1:
                lmap[i] == 0
            else:
                lmap[i] += lmap[i-1]+1

        for i in range(len(seats)-2, -1, -1):
            if seats[i] == 1:
                rmap[i] == 0
            else:
                rmap[i] += rmap[i+1]+1
        
        result = 0
        for key, value in lmap.items():
            if key == 0 or key == len(seats)-1:
                distance = max(value, rmap[key])
            else:
                distance = min(value, rmap[key])
            if distance > result:
                result = distance
        return result


class Solution(object):
    """O(n) two pointers"""
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans

class Solution(object):
    def maxDistToClosest(self, seats):
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans,seats.index(1))
        for seat, group in groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K+1)/2)

        return ans

solution = Solution()
seats = [1,0,0,0,1,0,1]
print(solution.maxDistToClosest(seats))
seats = [1,0,0,0]
print(solution.maxDistToClosest(seats))
seats = [0,0,0,1]
print(solution.maxDistToClosest(seats))
seats = [0,1,1,1,0,0,1,0,0]
print(solution.maxDistToClosest(seats))
seats = [1,0,0,1]
print(solution.maxDistToClosest(seats))
seats = [0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0]
print(solution.maxDistToClosest(seats))