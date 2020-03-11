#!/usr/bin/env python3
# practice interview questions in python3
# 2.5.2020

# Find the most frequent integer in an array

# first solution
def frequent(givenList) :
    tempDict = {}

    for i in range(0, len(givenList)):
        if str(givenList[i]) in tempDict:
            tempDict[str(givenList[i])] += 1
        else:
            tempDict[str(givenList[i])] = 1

    max = 0
    numbers = []
    for i in tempDict:
        if int(tempDict[i]) > max:
            numbers = [i]
            max = int(tempDict[i])
        elif int(tempDict[i]) == max:
            numbers.append(i)
    return [numbers, max]

# second solution
def mapping(givenList) :
    ans = ''
    # map frequencies
    m = [0]*len(givenList)
    for i in range(0, len(givenList)) :
        #m[givenList[i]]
        m[givenList[i]] += 1
        print(m)

    print(m)

    maxFrequency = max(m)

    for i in range(0, len(m)) :
        if m[i] == maxFrequency :
            ans += str(i) + ' '
    return ans

if __name__ == "__main__" :
    givenList = [1, 2, 3, 4, 4, 5, 6, 7, 1, 1, 8, 9, 9, 9, 9, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9]
    givenList.extend([11,11,11,11,11,11,11,11,11,11,11])

    # first solution
    ans = frequent(givenList)
    print("Most frequent integer(s) are " + str(ans[0]) + " with frequency: "+ str(ans[1]))

    # second solution
    print(mapping(givenList))
