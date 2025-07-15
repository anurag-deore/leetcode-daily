'''
Problem Name: 3136. Valid Word
Attempted : # 15-07-2025
'''
import re
class Solution:
    def isValid(self, word: str) -> bool:
        pattern = r'^(?=[A-Za-z0-9]{3,}$)(?=.*[AEIOUaeiou])(?=.*[B-DF-HJ-NP-TV-Zb-df-hj-np-tv-z]).*$'
        if re.match(pattern, word):
            return True
        else:
            return False