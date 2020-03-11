# problem 7
# 10001st prime
#
# 2.15.2020

count = 0
num = 1
st = 10001

while True:
    isPrime = True
    for i in range (2,num-1) :
        if num%i == 0 : # not a prime
            isPrime = False
            break
        else:
            continue

    if isPrime:
        count+=1

    if count==st:
        print(num)
        break
    else:
        num+=2
        continue
