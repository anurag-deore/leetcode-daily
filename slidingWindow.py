'''
Logic : to slide the window size, initially add the first window for given window_Size, here : window_sum = sum([4,6]) = 10
then in a loop subtract first element from window_sum and add next element, here : window_sum = sum([4,6]) - 4 + 1 = 7
then compare max and current window_sum and accordingly update.
'''

def slidingWindow(arr,window_size):
    n = len(arr)
    if(n < window_size):return -1
    
    window_sum = sum([arr[i] for i in range(window_size)])
    max_sum = window_sum

    for i in range(n-window_size):
        window_sum = window_sum - arr[i] + arr[i+window_size]
        max_sum = max(window_sum,max_sum)
    return max_sum

arr = [4,6,1,2]
window_size = 2
res = slidingWindow(arr,window_size)
if(res != -1):
    print("Max sum = ",res)
else:
    print("Error. Invalid Operation")