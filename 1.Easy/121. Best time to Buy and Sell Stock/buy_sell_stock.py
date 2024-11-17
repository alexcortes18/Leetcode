from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits = []

        # for i in range(len(prices)):
        #     current_buying = prices[i]
        #     for j in range(i+1,len(prices)):
        #         if j >= len(prices): break
        #         if prices[j] > current_buying:
        #             profits.append(prices[j] - current_buying)
        # if not profits: return 0

        # return max(profits)
        min_price = float('inf')  # Initialize with infinity
        max_profit = 0  # Initialize profit

        for price in prices:
            if price < min_price:
                min_price = price  # Update minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update maximum profit

        return max_profit