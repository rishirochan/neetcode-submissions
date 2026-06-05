class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = 0
        s = 1
        profit = 0
        while s < len(prices):
        # if the price is increasing we want to move second
            if prices[s] >= prices[f]:
                profit = max(profit, prices[s]-prices[f])
                s += 1
        # if decrease we want to move first
            else:
                f = s
                s += 1

        return profit