class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0


        for i in range(1, len(prices)):
            profit = prices[i] - minBuy
            if profit > maxProfit:
                maxProfit = profit

            if minBuy > prices[i]:
                minBuy = prices[i]
        
        return maxProfit