# https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    x = 0
    y = 0
    for j in moves:
        if j == 'U':
            x += 1
        elif j == 'D':
            x -= 1
        elif j == 'L':
            y += 1
        elif j == 'R':
            y -= 1
    return str(x == 0 and y == 0).lower()
    # alternate solution 
    # if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
    # return True


print(judgeCircle("LDRRLRUULR"))
