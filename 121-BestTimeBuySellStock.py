class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprice = prices[0]
        minprice = prices[0]
        profits = []
        for i in range(len(prices)):
            if prices[i] < minprice:
                maxprice = prices[i]
                minprice = prices[i]
            elif prices[i] > maxprice:
                maxprice = prices[i]
            profits.append(maxprice - minprice)
        return max(profits)
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,4,1]))
print(s.maxProfit([1,2]))