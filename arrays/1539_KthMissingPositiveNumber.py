from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cur, missing = 1, []
        for num in arr:
            while cur < num: 
                missing.append(cur)
                cur+=1
            cur+=1
        if k-1 in range(0, len(missing)): return missing[k-1]
        if not missing: return arr[-1]+k
        else: return arr[-1] + (k-len(missing))

class Solution:
    """LC Binary Search"""
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k