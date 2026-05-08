class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        - Initialize my max profit to 0, L=0 and r=0
        - While the right pointer is in size of array
        - Check if transcation is profitable ie prices[l]<prices[r]
        - If yes, compute the profit and find which one  is max
        - If transaction is not profitable,make l to be at r since we want to max profit
        - Increase r value
        - return max profit

        """
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
            else:
                l = r
            r += 1
        return maxProfit
       