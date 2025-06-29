# https://leetcode.com/problems/valid-mountain-array/

def isValidMountain(arr):
    i = 1
    n = len(arr)

    if(n < 3):
        return False

    while(i < n and arr[i] > arr[i-1]):
        i += 1
    if(i == 1 or i == n):
        return False
    while(i < n and arr[i] < arr[i-1]):
        i += 1
    return i == n


arr = [2, 1]
print(isValidMountain(arr))
