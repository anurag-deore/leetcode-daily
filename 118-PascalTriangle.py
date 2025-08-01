'''
Problem Name: 118. Pascal's Triangle
Attempted : # 01-08-2025
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            newRes = [0] + res[-1] + [0]
            res.append([newRes[j] + newRes[j+1] for j in range(len(newRes)-1)])
        return res

s = Solution()
print(s.generate(5))
