from collections import defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        stepmap = defaultdict(int)
        def climb(step):
            if step == 0: return 1
            if step < 0: return 0
            step1, step2 = -1, -1
            if step-1 in stepmap: step1 = stepmap[step-1]
            else:
                step1 = climb(step-1)
                stepmap[step-1] = step1
            if step-2 in stepmap: step2 = stepmap[step-2]
            else: 
                step2 = climb(step-2)
                stepmap[step-2] = step2
            return step1 + step2
        return climb(n)

solution = Solution()
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(45))