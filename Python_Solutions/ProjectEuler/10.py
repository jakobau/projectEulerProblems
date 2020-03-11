# problem 10
# Summation of primes
#
# completed: 3.11.2020

import math

number = 200000#2000000 # 2 million

count = 1
num = 1

while num < number :
    isPrime = True
    for i in range (2,num-1) :
        if num%i == 0 : # not a prime
            isPrime = False
            break
    if isPrime :
        count+=num
    num+=2

print(count)
