'''
Problem Name : 2094. Finding 3-Digit Even Numbers
Attempted : # 20-09-2025
'''
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        final = []
        for i in range(100,999,2):
            cp = digits.copy()
            count = 0
            for j in str(i):
                try:
                    if int(j) in cp:
                        count+=1
                        cp.remove(int(j))
                except:
                    continue
            if count == 3:
                final.append(i)
        return final
