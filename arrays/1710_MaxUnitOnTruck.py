from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        boxes, result = 0, 0
        for nbox, units in boxTypes:
            while nbox > 0 and boxes < truckSize:
                boxes += 1
                nbox -= 1
                result += units
        return result