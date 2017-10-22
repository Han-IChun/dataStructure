# -*- coding:utf-8 -*-

"""
Problem
Given an array of integers (positive and negative) find the largest continuous sum.

"""

def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    check_point = []
    arr = [0]+arr+[0]
    print arr
    for i in range(1,len(arr)):
        if arr[i]<0:
            check_point.append(i)
    check_point = [0]+check_point+[0]
    for j in range(len(check_point)-1):
        now = check_point[j]
        nextone = check_point[j+1]
        print sum(arr[now+1:nextone])
        
    return 
    
    






from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        print 'ALL TEST CASES PASSED'
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)