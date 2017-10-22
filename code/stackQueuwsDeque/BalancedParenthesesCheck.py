# -*- coding:utf-8 -*-

"""

A very common interview question is to begin by just implementing a Stack! Try your best to implement your own stack!
It should have the methods:
Check if its empty
Push a new item
Pop an item
Peek at the top item
Return the size

"""


class Stack(list):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        return self.items
        
    def pop(self):
        del self.items[len(self.items)-1]
        return self.items
    
    def peek(self):
        return self.items[-1]
    
    def sizeOf(self):
        return len(self.items)
    

        



"""
It's very common to be asked to implement a Queue class! The class should be able to do the following:
Check if Queue is Empty
Enqueue
Dequeue
Return the size of the Queue

"""
class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
        return self.items
        
    def dequeue(self):
        del self.items[0]
        return self.items
    
    def sizeOf(self):
        return len(self.items)




"""
implement Queues with Stack
"""

class Queue_useStack():
    
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def isEmpty(self):
        return self.s1 == []
    
    def enqueue(self,item):
        self.s1.append(item)
        return self.s1
        
    def dequeue(self):
        self.s2 = self.s1[::-1]
        self.s2.pop()
        self.s1 = self.s2[::-1]
        return self.s1
    
    def sizeOf(self):
        return len(self.s1)
    
    
#qs1 = Queue_useStack()
#print qs1.enqueue(1),qs1.enqueue(2),qs1.enqueue(3), qs1.dequeue(), qs1.sizeOf()

"""
Finally, implement a Deque class! It should be able to do the following:
Check if its empty
Add to both front and rear
Remove from Front and Rear
Check the Size
"""

class Deque(object):
    
    def __init__(self):
        self.list1 = []
        self.list2 = []
        
    def isEmpty(self):
        return self.list1 == []
    
    def addFront(self, item):
        self.list2 = self.list1[::-1]
        self.list2.append(item)
        self.list1 = self.list2[::-1]
        return self.list1
        
    def addRear(self, item):
        self.list1.append(item)
        return self.list1
    
    def removeFront(self):
        del self.list1[0]
        return self.list1
        
    def removeRear(self):
        self.list1.pop()
        return self.list1
    
    def sizeOf(self):
        return len(self.items)

    
# Run Tests
s = Stack()
print s.isEmpty(), s.push(1), s.push(2), s.push(3), s.pop(),s.push(3), s.peek(),s.pop(), s.sizeOf() 
    
q = Queue()
print q.isEmpty(),q.enqueue(1),q.enqueue(2),q.dequeue(),q.enqueue(3), q.sizeOf()
    
qs1 = Queue_useStack()
print qs1.enqueue(1),qs1.enqueue(2),qs1.enqueue(3), qs1.dequeue(),qs1.enqueue(3), qs1.sizeOf() 


dq1 = Deque()
print dq1.addFront(1),dq1.addFront(2),dq1.addRear(3), dq1.removeFront(),dq1.addFront(7), dq1.removeRear()