# https://leetcode.com/problems/count-primes/

'''
We use "Sieve Of Erathosthenes"
- Define a boolean array with all elements except 0,1 to be "TRUE" 
    ie consider all elements to be prime
'''
import math

def countPrimes(n):
    if(n<2):return 0
    isPrime = [True]*n
    isPrime[0] = isPrime[1] = False
    for i in range(2,int(math.ceil(math.sqrt(n)))):
        if (isPrime[i]):
            for multiples_of_i in range(i*i,n,i):
                isPrime[multiples_of_i] = False
    return sum(isPrime)

n = 10
print(countPrimes(n))