from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = 0
        result_arr = []
        length = len(digits)-1
        for index, digit in enumerate(digits):
            result += digit*pow(10, length-index)
        result += 1
        while result != 0:
            res_digit = result%10
            result_arr.insert(0, res_digit)
            result //= 10
        return result_arr

"""
finesse
num = int(''.join(map(str,digits)))+1
digit_string = str(num)
digit_map = map(int, digit_string)
return list(digit_map)
"""

solution = Solution()
digits = [1,2,3]
solution.plusOne(digits)
digits = [4,3,2,1]
solution.plusOne(digits)
digits = [9]
solution.plusOne(digits)