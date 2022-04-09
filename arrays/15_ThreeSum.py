from typing import List
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = set()
        nums.sort()

        for index, number in enumerate(nums):
            if number > 0:
                break
            if number in visited:
                continue
            visited.add(number)
            target = 0 - number
            self.twoSum(nums[index+1:], target, number, results)
        
        return results

    def twoSum(self, nums_arr, target, base, results):
        nmap = defaultdict(list)
        for index, number in enumerate(nums_arr):
            nmap[number].append(index)
        
        for index, number in enumerate(nums_arr):
            cur_target = target-number
            if nmap[cur_target] and cur_target == number:
                if len(nmap[cur_target]) > 1:
                    ritem = [base, cur_target, number]
                    ritem.sort()
                    if ritem not in results:
                        results.append(ritem)
            elif nmap[cur_target] and cur_target != number:
                ritem = [base, cur_target, number]
                ritem.sort()
                if ritem not in results:
                    results.append(ritem)
                
    

solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))