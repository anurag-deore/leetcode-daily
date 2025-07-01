'''
Problem Name: 1534. Count Good Triplets
Attempted : # 02-07-2025
'''

def countGoodTriplets(arr,a,b,c):
  goodtriplets = 0 
  for i in range(len(arr)-2):
    for j in range(i+1,len(arr)-1):
      if(abs(arr[i] - arr[j]) <= a):
        for k in range(j+1,len(arr)):
          if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
            goodtriplets +=1 
  return goodtriplets

print(countGoodTriplets([3,0,1,1,9,7],7,2,3))