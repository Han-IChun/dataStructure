# -*- coding:utf-8 -*-

"""

Anagram Check
Problem
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
For example:
"public relations" is an anagram of "crap built on lies."

"clint eastwood" is an anagram of "old west action"

Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".

"""

# this function do not consider repeat characters. It fails test.
def anagram1(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    for str1 in s1:
        if not str1 in s2:
            return False
    return True

# time complexity is O(n)
def anagram2(s1,s2): 
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    dic={}
    if not len(s1)==len(s1):
        return False
    for i in range(len(s1)):
        if s1[i] not in dic.keys():
            dic[s1[i]]=1
        else:
            dic[s1[i]]=dic[s1[i]]+1
            
    for i in range(len(s2)):
        if s2[i] not in dic.keys():
            dic[s2[i]]=1
        else:
            dic[s2[i]]=dic[s2[i]]-1
            
    return dic.values() == [0]*len(dic.values())




from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print "ALL TEST CASES PASSED"
        

# Run Tests
t2 = AnagramTest()
t2.test(anagram2)

