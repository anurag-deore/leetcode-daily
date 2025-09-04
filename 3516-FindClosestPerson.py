'''
Problem Name: 3516. Find Closest Person
Attempted : # 04-09-2025
'''

class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if (abs(z-x) == abs(z-y)):
            return 0
        elif (abs(z-x) < abs(z-y)):
            return 1
        else: 
            return 2

