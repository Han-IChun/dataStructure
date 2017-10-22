# -*- coding:utf-8 -*-

"""
Problem
Given an integer array, output all the unique pairs that sum up to a specific value k.
So the input:
pair_sum([1,3,2,2],4)

would return 2 pairs:
 (1,3)
 (2,2)

NOTE: FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

"""

# time complexity O(n^2). Not very efficient but pass tests.
def pair_sum1(arr,k):
    pairs = {}
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == k:
                pair = sorted([arr[i], arr[j]])
                pairs[str(pair)]=1
    return len(pairs.keys())



def pair_sum2(arr,k):
    uniqueNum_dic = {}
    pairs = []
    for ele in arr:
        uniqueNum_dic[minus]=1
    for key in uniqueNum_dic.keys():
        minus = 

        if minus in arr:
            pairs.append([ele, minus])
    print pairs
    return len(pairs)


def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Sets for tracking
    seen = set()
    output = set()
    
    # For every number in array
    for num in arr:
        
        # Set target difference
        target = k-num
        
        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)
        
        else:
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
    
    return len(output)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print 'ALL TEST CASES PASSED'
        
#Run tests
t1 = TestPair()
t1.test(pair_sum1)
t2 = TestPair()
t2.test(pair_sum2)
