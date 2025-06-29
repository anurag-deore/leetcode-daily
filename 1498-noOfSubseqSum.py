'''
Problem Name: 1498. Number of subsequences that satisfy the given sum condition
Attempted : # 29-06-2025
'''

def all_subs(inputArray,outputArray,index):
    print("\n\n Op ARR => ",outputArray,"\nCurr Index =>",index)
    if(len(inputArray)==index):
        print(outputArray)
        return
    outputArray.append(inputArray[index])
    all_subs(inputArray,outputArray,index+1)
    outputArray.pop()
    all_subs(inputArray, outputArray, index + 1)



all_subs([1,3,6,8],[],0)