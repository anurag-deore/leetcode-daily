'''
Problem Name: 3304. Find the K-th Character in String Game I
Attempted : # 03-07-2025
'''

class Solution:
    def kthCharacter(self, k: int) -> str:
      str = "a"
      while len(str) < k:
         str += self.genNext(str)
      print(str)
      return str[k-1]
    
    def genNext(self,s:str) -> str:
      newS = ""
      for i in s:
        newS += chr((ord(i)+1))
      return newS
    

sol = Solution()
print(sol.kthCharacter(26))