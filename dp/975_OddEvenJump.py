"""
Brute Force TLE on 60/65
"""
from typing import List

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        cur_jump = 1
        valid_count = 0
        odd_valid = []
        odd_invalid = []
        even_valid = []
        even_invalid = []
                
        for index, number in enumerate(arr):
            # print(f" ----- For Case Number {number} -----")
            odd_visited = []
            even_visited = []
            completed = False
            bigger = []
            smaller = []
            cur_jump = 1

            while not completed:
                # print(f"Current number is {number} at {index}")
                if number == arr[-1]:
                    completed = True
                    valid_count += 1
                    continue
                if cur_jump % 2 != 0:
                    check = (index, number)

                    if check in odd_valid:
                        # print(print(f"Current number is {number} at {index} is already validated"))
                        completed = True
                        valid_count+=1
                        continue
                    elif check in odd_invalid:
                        # print(print(f"Current number is {number} at {index} is already Invalidated"))
                        completed = True
                        continue

                    odd_visited.append((index, number))
                    # print("odd jump")
                    for map_index, map_number in enumerate(arr):
                        if map_number >= number and map_index > index:
                            bigger.append({"number": map_number, "index": map_index})
                    if len(bigger) == 0:
                        completed = True
                        odd_invalid += odd_visited
                        # print("Hit end, not valid")
                        continue
                    bigger.sort(key = lambda x: x["number"])
                    # print(bigger)
                    odd_jump_number = bigger[0]["number"]
                    number = odd_jump_number
                    index = bigger[0]["index"]
                    if odd_jump_number == arr[-1]:
                        completed = True
                        valid_count+=1
                        odd_valid += odd_visited
                        # print("Hit end, Valid")

                elif cur_jump % 2 == 0:
                    check = (index, number)
                    
                    if check in even_valid:
                        # print(print(f"Current number is {number} at {index} is already Validated"))
                        completed = True
                        valid_count+=1
                        continue
                    elif check in even_invalid:
                        # print(print(f"Current number is {number} at {index} is already Invalidated"))
                        completed = True
                        continue

                    even_visited.append((index, number))
                    # print("even jump")
                    for map_index, map_number in enumerate(arr):
                        if map_number <= number and map_index > index:
                            smaller.append({"number": map_number, "index": map_index})
                    if len(smaller) == 0:
                        completed = True
                        even_invalid += even_visited
                        # print("Hit end, not valid")
                        continue
                    smaller.sort(key = lambda x: x["number"])
                    even_jump_number = smaller[-1]["number"]
                    number = even_jump_number

                    for item in smaller:
                        if item["number"] == number:
                            index = item["index"]
                            break
                    
                    if even_jump_number == arr[-1]:
                        completed = True
                        valid_count+=1
                        even_valid += even_visited
                        # print("Hit end, Valid")

                cur_jump += 1
                bigger = []
                smaller = []
        
        return valid_count