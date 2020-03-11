# problem 2
# Even Fibonacci Numbers
#
# 2.15.2020

fu1 = 1
fu2 = 2
fu3 = 0

sum = fu2

while True :
    fu3 = fu1 + fu2
    if fu3%2 == 0:
        sum += fu3

    if fu3 >= 4000000:
        break

    fu1 = fu2
    fu2 = fu3

print(sum)
