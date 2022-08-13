class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k: stack.pop()
            else: stack.append([c, 1])
        return ''.join(c * k for c, k in stack)