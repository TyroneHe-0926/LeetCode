from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp, maxp, profit = [0, prices[0]], [0, prices[0]], 0
        for index, price in enumerate(prices):
            if price < minp[1]: minp[0], minp[1] = index, price
            if price > maxp[1]: maxp[1] = price
            if minp[0] > maxp[0]: maxp[0], maxp[1] = minp[0], minp[1]
            cur_profit = maxp[1] - minp[1]
            profit = max(cur_profit, profit)
        return profit

solution = Solution()
prices = [1,4,5,0,5,6]
print(solution.maxProfit(prices))