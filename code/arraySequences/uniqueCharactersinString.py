# -*- coding:utf-8 -*-

"""
Problem
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

"""

# time complexity O(n)

def uni_char(s1):
    if len(s1)==0:
        return True
    
    d = defaultdict(int)
    for cha in s1:
        d[cha] += 1
    isDuplicated = any(d.values()>1)
    return not isDuplicated

def uni_char1(s):
    return len(set(s)) == len(s)



def uni_char2(s):
    chars = set()
    for let in s:
        # Check if in set
        if let in chars:
            return False
        else:
            #Add it to the set
            chars.add(let)
    return True



"""
RUN THIS CELL TO TEST YOUR CODE>
"""
from nose.tools import assert_equal


class TestUnique(object):

    def test(self, sol):
        assert_equal(sol(''), True)
        assert_equal(sol('goo'), False)
        assert_equal(sol('abcdefg'), True)
        print 'ALL TEST CASES PASSED'
        
# Run Tests
t = TestUnique()
t.test(uni_char)