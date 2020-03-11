# problem 5
# smallest multiple
#
# 2.15.2020

numbers = [2,3,5,7,11,17,19]
numbersTen = [2,3,4,5,6,7,8,9,10]

for a in range(20,100000000000000,20):
    divEven = True
    for i in range(2,20):
        if a%i != 0 :
            divEven = False
            break
        else:
            continue
    if divEven :
        print(a)
        break
    else:
        continue
