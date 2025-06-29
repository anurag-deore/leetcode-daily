# https://leetcode.com/problems/move-zeroes/submissions/
def movezerostoend(arr):
    j = 0
    n = len(arr)
    for i in range(n):
        if(arr[i] != 0):
            arr[j] = arr[i]
            j+=1
    for i in range(j,n):
        arr[i] = 0
    
    print(arr)

arr = [0,3,0,2,10,2,0,1,0,2,0]
movezerostoend(arr)