class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = 30000
        profit = 0
        for price in prices:
            if stock > price:
                stock = price
            elif stock < price:
                profit += price - stock
                stock = price
        return profit