from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s = s[::-1]


class Solution:
    """Legit recursion"""
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)

class Solution:
    """Legit two pointers"""
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1