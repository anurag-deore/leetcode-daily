'''
Problem Name : 2942. Find Words Containing Character
Attempted : # 22-08-2025

'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = []
        for j in range(len(words)):
            if(x in words[j]):
                output.append(j)
        return output
