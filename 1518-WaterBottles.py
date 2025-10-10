'''
Problem Name: 1518. Water Bottles
Attempted : # 10-10-2025
'''
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalBottles = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            totalBottles += emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange + emptyBottles // numExchange
        return totalBottles

s = Solution()
print(s.numWaterBottles(9,3))
print(s.numWaterBottles(15,4))
