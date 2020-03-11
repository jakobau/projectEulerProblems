#!/usr/bin/env python3
# practice interview questions in python3
# 2.5.2020
# pairs_inArray_withSum_equalTo_10.py

# Find pairs in an integer array whose sum is equal to 10
# (bonus: do it in linear time)
import timeit
import time
from random import seed
from random import random

# test for each possibility:
#   - can make n(n-1) pairs
#   - not including pairs of an integer and itself

# above possible pairs is 15(14) = 210

# plan: test for all pair possibilities at index 0, then move index 0 to end
#       of list and continue until length of array.
# - not linear run time...

def countPairs( array ) :
    pairs = []
    count = len( array )

    while count > 0 :
        # test at index 0
        for i in range( 1, len(array) ) :
            if ( array[0] + array[i] ) == 10 :
                pairs.append( [array[0], array[i]] )
        # move index 0 to index maxLength
        array.append( array.pop(0) )
        # next integer
        count -= 1

        return count

# test run-time
def test_runtime(funcName) :
    x = "countPairs( array )"
    for i in range( 1, 10 ) :
        # make array of random integers from 1 - 10
        for j in range( 10, 100, 10 ) :
            array.append( int(random() * 10) )

        # change
        if funcName == "faster( array, 10 )":
            x = "faster( array, 10)"

        # time function
        mytime = timeit.Timer(x, setup="from __main__ import faster, countPairs, array")
        mytime = mytime.timeit( number=1000)
        mytime = mytime/1000
        #print( mytime ) # print time
        print( mytime / ( len(array)*len(array) ) ) # print slope, in this case runtime is O(n^2)
        print("")

    # differrent way to time a function
    """
    start_time = time.time()
    countPairs(array)
    print("--- %s seconds ---" % ( time.time() - start_time ) )
    """

# runtime of O(n)
def faster( arr, sum ):
    n = len(arr)
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        #m[arr[i]]
        m[arr[i]] += 1

    twice_count = 0

    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):

        twice_count += m[sum - arr[i]]

        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1

    # return the half of twice_count
    return int(twice_count / 2)

if __name__ == "__main__" :
    seed(1)
    array = [ 1, 10, 0, 9, 4, 5, 6, 7, 6, 5, 4, 3, 2, 8, 9 ]

    # runtime of O(n^2)

    ans = countPairs( array )
    print( "number of pairs found: " + str( ans ) )

    #if ( input("See runtime? y/n: ") == "y" ) :
    test_runtime("countPairs")


    # runtime of O(n)
    print( "number of pairs found: " + str( faster( array, 10 ) ) )

    #if ( input("See runtime? y/n: ") == "y" ) :
    test_runtime("faster")
