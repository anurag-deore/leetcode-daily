'''
Problem Name: 1717. Maximum Score From Removing Substrings
Attempted : # 24-07-2025
'''
# Dry run example:
# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Since y > x, we remove "ba" (score 5) first, then "ab" (score 4).
# Step 1: Remove "ba":
#   - After removing all "ba", string becomes "cdbcbbaaabab" -> "cdbcbaaab"
#   - Score from "ba" removals: 2 * 5 = 10
# Step 2: Remove "ab":
#   - After removing all "ab", string becomes "cdbcbaaab" -> "cdbcbaa"
#   - Score from "ab" removals: 1 * 4 = 4
# Total score: 10 + 4 = 14

#approach 1 - times out
        # bigVal = x if x > y else y
        # smallval = y if x > y else x
        # maxstr = "ab" if x > y else "ba"
        # secondMaxstr = "ba" if x > y else "ab" 
        # replaced = 0
        # val = 0
        # occurences = -1
        # while occurences != 0:
        #   h = [m.start() for m in re.finditer(maxstr,s)]
        #   s = s.replace(maxstr,"")
        #   occurences = len(h)
        #   replaced += occurences
        # val += replaced * bigVal
        # occurences = -1
        # replaced = 0
        # while occurences != 0:
        #         h = [m.start() for m in re.finditer(secondMaxstr,s)]
        #         s = s.replace(secondMaxstr,"")
        #         occurences = len(h)
        #         replaced += occurences
        # val += replaced * smallval
        # return val

import re
class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    # This solution greedily removes the higher scoring substring ("ab" or "ba") first using a stack,
    # then removes the other substring, maximizing the total score.
    def remove_pair(s, first, second, score):
      stack = []
      total = 0
      for c in s:
        print(stack)
        if stack and stack[-1] == first and c == second:
          stack.pop()
          total += score
        else:
          stack.append(c)
      return ''.join(stack), total

    # Remove the higher value pair first
    if x >= y:
      s, score1 = remove_pair(s, 'a', 'b', x)
      _, score2 = remove_pair(s, 'b', 'a', y)
    else:
      s, score1 = remove_pair(s, 'b', 'a', y)
      _, score2 = remove_pair(s, 'a', 'b', x)
    return score1 + score2
    
s = Solution()
print(s.maximumGain("cdbcbbaaabab", 4, 5))
# print(s.maximumGain("aabbaaxybbaabb", 5, 4))