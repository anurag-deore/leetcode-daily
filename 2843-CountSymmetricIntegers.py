'''
Problem Name:  2843. Count Symmetric Integers
Attempted: # 05-09-2025
'''
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                s = [int(j) for j in str(i)]
                first_half  = sum(s[:len(s)//2])
                second_half = sum(s[len(s)//2:])
                if first_half == second_half:
                    print(first_half,s[:len(s)//2])
                    count+=1
        return count
