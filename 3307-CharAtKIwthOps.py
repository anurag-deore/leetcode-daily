'''
Problem Name: 3307. Find the K-th Character in String Game II
Attempted : # 05-07-2025
'''

'''
BRUTE FORCE:
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        start="a"
    
        def genNextStr(s:str):
            newS=""
            for i in s:
                newS += chr((ord(i)+1))
            return newS

        for i in range(len(operations)):
            if operations[i] == 0:
                start = start + start
            elif operations[i] == 1:
                start = start + genNextStr(start)
        return start[k-1]
'''

'''
ACTUAL SOLUTION:
'''
import math

class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        count = 0
        while k != 1:
            index = math.ceil(math.log(k,2))-1
            maxLen = pow(2,index)
            k = k - maxLen
            if(operations[index]):
              count +=1  
        
        return chr(ord("a") + ord(chr(count % 26)))
    
s = Solution()
# a = s.kthCharacter(456402,[0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,1])
# a = s.kthCharacter(10,[0,1,0,1])
a = s.kthCharacter(4,[1,0])
print(a)