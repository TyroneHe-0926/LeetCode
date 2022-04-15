def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        high, low, mid = n, 0, None
        while low <= high:
            mid = (low+high)//2
            if not isBadVersion(mid): low = mid+1
            else: high = mid - 1
        return mid