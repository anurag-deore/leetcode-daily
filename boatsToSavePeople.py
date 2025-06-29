# https://leetcode.com/problems/boats-to-save-people/

def boatsTosave(people, limit):
    people.sort()
    boats = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
            boats += 1
        else:
            right -= 1
            boats += 1
    return boats


people =  [3,5,3,4]
limit = 5
print(boatsTosave(people, limit))
