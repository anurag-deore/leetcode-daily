'''
Problem Name: 1295. Find Numbers with Even Number of Digits 
Attempted : # 21-08-2025
'''


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        x=0
        for i in nums:
            if(len(str(i)))%2==0:
                x+=1
        return x 
