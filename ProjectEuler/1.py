#!/usr/bin/python
# problem 1
# If we list all the natural numbers below 10 that are multiples of
#       3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# 2.14.2020

n = 1000

x = []

for i in range(1,n) :
    if i%3 == 0:
        x.append(i)
    elif i%5 == 0:
        x.append(i)


print(x)
print(sum(x))
