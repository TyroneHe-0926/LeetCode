from typing import List
from collections import defaultdict
import random

class Solution:
    """Hashmap index -> percentile TLE ... rly be tle on these O(n)s too i guess"""
    def __init__(self, w: List[int]):
        self.weights = defaultdict(tuple)
        self.sum = sum(w)
        start = 0
        for index, weight in enumerate(w):
            end = weight*100 // self.sum
            self.weights[index] = (start, start+end)
            self.end = start + end
            start = start+end+1


    def pickIndex(self) -> int:
        target = random.randint(0,self.end)
        for index, (start, end) in self.weights.items():
            if target in range(start ,end+1): return index

class Solution:
    """Gonna use a binary search with just a number percentile to reduce pick to O(logn)"""
    def __init__(self, w: List[int]):
        self.weights = []
        start, self.end = 0, 0
        for weight in w:
            start += weight
            self.weights.append(start)
        self.end = start
        print(self.weights)


    def pickIndex(self) -> int:
        # should start with one cuz the weight of the first index cant start with 0 ever
        # if we include 0 thats like boosting the weight of index 0 by 1

        target = random.randint(1,self.end)
        low, high = 0, len(self.weights)
        while low <= high:
            mid = (low+high)//2
            if self.weights[mid] < target:
                low = mid + 1
            elif self.weights[mid] > target:
                high = mid - 1
            else:
                return mid
        return low