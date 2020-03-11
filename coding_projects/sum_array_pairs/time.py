#!/usr/bin/env python3
# time.py - uses the timeit module, prob1.py and prob2.py to create
#			and write files 1.out and 2.out.
# Jakob Au, ID:jda92
# 1/27/2020
#

import timeit
import pairs_inArray_withSum_equalTo_10
from random import seed
from random import random

seed(1)
array = []
def test_runtime(funcName) :

    f= open("output.out","w+")

    for i in range( 100, 1000, 100 ) :

        global array

        # make array of random integers from 1 to i
        for j in range( 1, i ) :
            array.append( int(random() * j) )

        # figure out which function to run
        x = "faster(array,10)"

        if funcName == "faster":
            x = "faster( array, 10)"
        elif funcName == "countPairs":
            x = "countPairs( array )"

        #time function
        setupStr = "from pairs_inArray_withSum_equalTo_10 import faster, countPairs; from __main__ import array"
        mytime = timeit.Timer(x, setup=setupStr)
        mytime = mytime.timeit( number=1000)
        mytime = mytime/1000

        f.write(str(i)+" "+str(mytime)+"\n")

        #print( mytime ) # print time
        #print( mytime / ( len(array)*len(array) ) ) # print slope, in this case runtime is O(n^2)
        #print("")

    f.close()
    # differrent way to time a function
    """
    start_time = time.time()
    countPairs(array)
    print("--- %s seconds ---" % ( time.time() - start_time ) )
    """
if __name__ == "__main__" :

    test_runtime("countPairs")
