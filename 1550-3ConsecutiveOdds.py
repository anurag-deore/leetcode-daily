'''
Problem Name : 1550. Three Consecutive Odds
Attempted : # 18-09-2025
'''
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i%2 != 0:
                count+=1
            else: count = 0
            if count == 3:
                return True
        return False
