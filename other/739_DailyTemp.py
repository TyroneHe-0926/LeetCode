from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0]

        res, temp = [], [0]
        last = temperatures[0]

        for temperature in temperatures[1:]:
            if temperature > last: 
                temp = [i+1 for i in temp]
                for i in temp: res.append(i)
                temp = []
                last = temperature
            else:
                temp = [i+1 for i in temp]
            temp.append(0)
            print(res, temp)

"""
lc
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer
"""




s = Solution()
s.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
# s.dailyTemperatures(temperatures = [30,40,50,60])
# s.dailyTemperatures(temperatures = [40, 30, 20, 10])