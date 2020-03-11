# problem 9
# Special Pythagorean triplet
#
# completed: 3.11.2020

import math

# c = math.sqrt(a*a + b*b)

# tests all possible values to find a + b + c = 1000
for i in range(1,1000) :
    a = i
    for ii in range(i,1000) : # b > a
        b = ii
        if math.sqrt(a*a + b*b) + a + b == 1000 :
            print(a*b*math.sqrt(a*a + b*b))
