from typing import List
from itertools import groupby

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        groups = [list(g)[-1] for _, g in groupby(intervals, key=lambda x: x[0])]
        merged = []
        for group in groups:
            group.sort(key=lambda x: x[1])
            start, end = group[-1]
            merge = False
            for time in merged:
                if start > time:
                    if start <= merged[time] and end >= merged[time]:
                        merged[time] = end
                        merge = True
                    elif start <= merged[time] and end <= merged[time]:
                        merge = True
            if not merge:
                merged[start] = end
        return [[time, merged[time]] for time in merged]

class LeetcodeSortSolution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for start, end in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], end)

        return merged

solution = Solution()
print(solution.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))
print(solution.merge(intervals = [[1,4],[0,4]]))
print(solution.merge(intervals = [[1,18],[5,24],[2,10],[1,3]]))