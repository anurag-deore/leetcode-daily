'''
Problem Name: 2894. Divisible and Non-divisible Sums Difference
Attempted : # 15-07-2025
'''

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(1,n+1):
            if(i%m == 0):
               num1+=i
            else:
              num2+=i  
        return num2 - num1
  
s = Solution()
print(s.differenceOfSums(10,3))