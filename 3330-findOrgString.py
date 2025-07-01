'''
Problem Name: 3330. Find the Original Typed String I
Attempted : # 01-07-2025
'''
def possibleStringCount(word: str) -> int:
    count = 1  
    for i in range(1, len(word)):
        if word[i - 1] == word[i]:
            count += 1
    return count
        

print(possibleStringCount("ere"))
print(possibleStringCount("abbccca"))