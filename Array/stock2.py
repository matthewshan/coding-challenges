from typing import List

class Solution:
    # Peak Valley Approach
    def maxProfit(self, prices: List[int]) -> int:
        i: int = 0
        valley: int = prices[i]
        peak: int = prices[i]
        max_profit = 0
        while i < len(prices) - 1:
            # Find a valley (local min) - Buy Low
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]

            # Find a peak (local max) - Buy High
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]

            # Add the potential Profit
            max_profit += peak - valley
        return max_profit

s = Solution()
ex1 = s.maxProfit([7,1,5,3,6,4]) # 7
ex2 = s.maxProfit([1,2,3,4,5]) # 4
ex3 = s.maxProfit([7,6,4,3,1]) # 0

print(ex1, ex2, ex3)