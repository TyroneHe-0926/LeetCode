"""Sliding Window Question"""
from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fmap = defaultdict(dict)
        result = 0
        results = []
        last_visited = -1
        for index, fruit in enumerate(fruits):
            count = 1
            result = 0

            if fmap[fruit]:
                count += fmap[fruit]["count"]
            
            fmap[fruit]["index"] = index
            fmap[fruit]["count"] = count

            if len(fmap) == 3:
                del_index = -1 
                for item in fmap:
                    if item != last_visited:
                        del_index = fmap[item]["index"]
                        del fmap[item]
                        break
                    else:
                        fmap[item]["count"] -= 1

                for item in fmap:
                    if fmap[item]["index"] != index:
                        set_count = index - del_index
                        # print(f"Setting {item} to {set_count}")
                        fmap[item]["count"] = set_count-1

            for item in fmap:
                item_count = fmap[item]["count"]
                # print(f"Result is {item} with count {item_count}")
                result += item_count
                results.append(result)
            
            # print(result)
            last_visited = fruit

        # print(results)
        return max(results)

if __name__ == "__main__":
    solution = Solution()
    fruits2 = [0,1,2,2]
    fruits3 = [1,2,3,2,2]
    # solution.totalFruit(fruits2)
    # solution.totalFruit(fruits3)
    fc1 = [1,0,0,0,1,0,4,0,4]
    fc2 = [0,1,6,6,4,4,6]
    fc3 = [1,0,29,29,29,29,29,29,0,0,29,8,8,29,8,29,8,8,15,8,8,15,15,8,15,15,8,8,7,5]
    solution.totalFruit(fc1)
    solution.totalFruit(fc2)
    solution.totalFruit(fc3)

class LCSolution(object):
    def totalFruit(self, tree):
        count = defaultdict(int)
        result, i = 0, 0
        for j, v in enumerate(tree):
            count[v] += 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            result = max(result, j-i+1)
        return result
