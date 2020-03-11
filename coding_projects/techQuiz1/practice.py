#!/usr/bin/env python3
# practice interview questions in python3
# 2.5.2020


# python script
if __name__ == "__main__" :
    arr1 = [1,2,3,4,5]
    arr2 = [2,3,1,0,5,8]
    num = [ ]

    # map out numbers in array
    map1 = [0] * (max(arr1)+1) # length is the max of the array size + 1
    map2 = [0] * (max(arr2)+1)

    # fill out map1
    for i in range(0, len(arr1)) :
        map1[arr1[i]] += 1
        print(map1)

    # fill out map2
    for j in range(0, len(arr2)) :
        map2[arr2[j]] += 1
        print(map2)

    # test for map1[i] if map2 has the value
    for i in range(0, len(arr1)) :
        # if map2 doesnt have a map1 value
        if map1[i] > 0 and map2[i] == 0:
            num.append(str(i))

    # a list of numbers that arr1 has but not arr2
    print(num)
