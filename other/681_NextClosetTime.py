class Solution:
    def nextClosestTime(self, time: str) -> str:
        d1, d2, d3, d4 = int(time[0]), int(time[1]), int(time[3]), int(time[4])
        try:
            new_4 = min(x for x in [d1, d2, d3] if x > d4)
            return f"{d1}{d2}:{d3}{new_4}"
        except ValueError:
            pass

        try:
            new_3 = min(x for x in [d1, d2, d4] if x > d3 and x < 6)
            new_4 = min([d1, d2, d3, d4])
            return f"{d1}{d2}:{new_3}{new_4}"
        except ValueError:
            pass

        try:
            new_2 = min(x for x in [d1, d3, d4] if x > d2) if d1 != 2 else min(x for x in [d1, d3, d4] if x > d2 and x < 4)
            rest = min([d1,d2,d3,d4])
            return f"{d1}{new_2}:{rest}{rest}"
        except ValueError:
            pass
        
        try:
            new_1 = min(x for x in [d1,d2,d3,d4] if x < 3)
            if d1 == 1:
                return f"2{new_1}:{new_1}{new_1}" if 2 in [d1,d2,d3,d4] else f"{new_1}{new_1}:{new_1}{new_1}"
            elif d1 == 2:
                return f"{new_1}{new_1}:{new_1}{new_1}"
            elif d1 == 0:
                new_1 = min(x for x in [d2,d3,d4] if x < 3)
                return f"{new_1}0:00"
        except ValueError:
            return time


import random
solution = Solution()
random1, random2, random3, random4 = random.randint(0,2), random.randint(0,4), random.randint(0,5), random.randint(0,9)
random_time = f"{random1}{random2}:{random3}{random4}"
print("Genearated Time is: "+random_time)
print(solution.nextClosestTime("23:49"))