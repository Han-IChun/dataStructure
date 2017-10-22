# -*- coding:utf-8 -*-

"""
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.
The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.

"""

# time complexity O(n)

def compress(s1):
    result=[]
    if len(s1)==0:
        return ''
    
    d = defaultdict(int)
    for cha in s1:
        d[cha] += 1
    for key in sorted(d.keys()):
        result.append(key)
        result.append(str(d[key]))
    return ''.join(result)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal
from collections import defaultdict
class TestCompress(object):

    def test(self, sol):
        assert_equal(sol(''), '')
        assert_equal(sol('AABBCC'), 'A2B2C2')
        assert_equal(sol('AAABCCDDDDD'), 'A3B1C2D5')
        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestCompress()
t.test(compress)