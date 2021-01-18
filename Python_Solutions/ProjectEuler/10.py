#!/usr/bin/python
# problem 10
# Summation of primes
#
# completed: 3.11.2020

import math

number = 200000 # 2 million

answer = 3
num = 3
primeNums = [1,2]
count = 2

while num < number :
    isPrime = True
    print(str(num))

    #for i in range (3,math.ceil((num-1)/2),2) :
    #    if num%i == 0 : # not a prime
    #        isPrime = False
    #        break
    #for i in range (2,math.ceil(len(primeNums)/2)) :

    for i in range (2,math.ceil(len(primeNums)/2)) :
        if num%primeNums[i] == 0 :
            isPrime = False
            break

    if isPrime :
        primeNums.append(num)
        answer+=num
        count+=1
    num+=2

print("Number of Primes: " + str(count))
print("Answer: " + str(answer))
#print("Prime Numbers: " + str(primeNums))