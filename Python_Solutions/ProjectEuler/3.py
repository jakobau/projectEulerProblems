# problem 3
# Largest prime factor
#
# 2.15.2020

# Note: prime numbers are only divisable by itself and one

import math

num = 600851475143
factor = []
primeF = []

# under the square root
for i in range(3, int(math.sqrt(num))) :
    if num%i == 0:
        other = int(num/i)
        factor.append(i)
        factor.append(other)

#factor.sort()

for i in factor :
    isPrime = True
    for j in range(3, i-1) :
        if (i%j == 0) : # not prime
            isPrime = False
            break
    if isPrime :
        primeF.append(i)

print(primeF)
