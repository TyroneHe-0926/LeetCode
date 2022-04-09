from typing import List
from collections import defaultdict, Counter
from math import comb

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mp, ans, l, = defaultdict(int), 0, len(arr)

        for x in range(l-1):
            for y in range(x+1,l):
                diff=target-arr[x]-arr[y]
                ans+=mp[diff]
            mp[arr[x]]+=1
                
        return ans%(10**9+7)

def threeSumMulti(self, arr, target):
	c = Counter(arr)

	# u as the unique set
	u, ct = sorted(c.keys()), 0

	for i in range(len(u)):
		j, res = i, target - u[i]

		# as long as ui <= uj <= uk, and j in the range
		while j < len(u) and u[j] <= res - u[j]:
			uk = res - u[j]

			# if ui <= uj <= uk & ui + uj + uk == target
			if uk in u:
				temp = Counter([u[i], u[j], uk])

				# if ui < uj < uk, 3 distinct numbers
				if len(temp.keys()) == 3:   ct += c[u[i]] * c[u[j]] * c[uk]

				# if ui = uj < uk or ui < uj = uk, 2 distinct numbers
				elif len(temp.keys()) == 2: ct += comb(c[u[i]], temp[u[i]]) * comb(c[uk], temp[uk])

				# if ui = uj = uk
				else:   ct += comb(c[u[i]], temp[u[i]])
			j += 1

	return ct % (10**9 + 7)


solution = Solution()
print(solution.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
# print(solution.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))