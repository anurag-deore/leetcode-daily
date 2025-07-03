'''
Problem Name: 2138. Divide a String Into Groups of Size k
Attempted : # 03-07-2025
'''

class Solution:
  def divideString(self, s: str, k: int, fill: str) -> List[str]:
    n = len(s)
    newlist = []
    i = 0
    if(n%k) != 0:
        c = int(len(s)/k)+1
        remaining = c * k - n
        s = s + fill * remaining
    while i < len(s):
      newlist.append(s[i:i+k])
      i+=k
    return newlist