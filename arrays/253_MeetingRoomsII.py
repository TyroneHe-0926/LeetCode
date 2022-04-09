from typing import List
from collections import deque

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count, avalible = 0, deque([])
        intervals.sort(key=lambda x: x[0])
        for (start, end) in intervals:
            if not(any(start >= i for i in avalible)):
                count+=1
                avalible.append(end)
            else:
                for i, number in enumerate(avalible):
                    if number <= start:
                        avalible[i] = end
                        break
        return count

soln = Solution()
intervals = [[26,29],[19,26],[19,28],[4,19],[4,25]] #3
print(soln.minMeetingRooms(intervals))
intervals = [[4,18],[1,35],[12,45],[25,46],[22,27]] #4
print(soln.minMeetingRooms(intervals))
intervals = [[2,11],[6,16],[11,16]] #2
print(soln.minMeetingRooms(intervals))
intervals = [[1,5],[8,9],[8,9]] #2
print(soln.minMeetingRooms(intervals))
intervals = [[9,10],[4,9],[4,17]] #2
print(soln.minMeetingRooms(intervals))
intervals = [[12,13],[8,14],[6,9]] #2
print(soln.minMeetingRooms(intervals))
intervals = [[6,10],[13,14],[12,14]] #2
print(soln.minMeetingRooms(intervals))
intervals = [[15,16],[10,15],[16,25]] #1
print(soln.minMeetingRooms(intervals))
intervals = [[1,8],[6,20],[9,16],[13,17]] #3
print(soln.minMeetingRooms(intervals))
