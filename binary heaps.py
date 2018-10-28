#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:24:33 2018

@author: kefei
"""

class Stack:
    def __init__(self):
        self.items = []  # data structure
        
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
            
        item = self.items[-1]
        del self.items[-1]
        return item
        # return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items) 
    
class BinaryHeap:
    """min heap implementation
    
    Root node has minimum value in tree
    """
    def __init__(self,n):
        self.heap_list = [0]
        self.current_size = 0
        self.max_size = n
        
    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                tmp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i //= 2
            
    def insert(self, k):
        """Add a new condition that when the size of heap greater than n,
        delete the greatest priority and insert the new value into the heap
        """
        if self.current_size >= self.max_size:  # check if the size is larger than the maximum size
            index = self.current_size // 2
            for i in range(index+1, self.max_size+1):
                if(self.heap_list[i] > self.heap_list[index]):
                    index = i
            
            self.heap_list[index] = k
            self.perc_up(index)
        else:
            self.heap_list.append(k)
            self.current_size += 1
            self.perc_up(self.current_size)
        
    def perc_down(self, i):
        while (i * 2) <=  self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
                
            i = mc
            
    def min_child(self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2  # left child of parent node at i
            else:
                return i*2+1 # right child of parent node at i
            
    def del_min(self):
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]  # or, self.heap_list[self.current_size]
        self.heap_list.pop()  # pop out the mo
        self.current_size -= 1
        self.perc_down(1)
        return retval
    
    def build_heap(self, alist):
        i = len(alist)//2
        self.current_size = len(alist)
        self.heap_list = [0] + alist  # copies alist
        while i > 0:
            self.perc_down(i)
            i -= 1
            
class PriorityQueue:
    """A new class called PriorityQueue, based on the BinaryHeap class.
    The heap will be a min heap, meaning the smallest priority value is the root of the tree,
    and thus has the highest priority."""
    
    def __init__(self, n):
        """Initialize an empty priority queue, with a maximum size of n."""
        self._bHeap = BinaryHeap(n)
        self._index = 0
        
    def enqueue(self,val,priority):
        """Adds val to the priority queue with the specified priority. 
        Smaller priority numbers correspond to higher priorities,
        which means that all priority 1 elements are dequeued before any priority 2 elements.

        Negative priorities are allowed and are not treated differently from other values. 
        That is, a priority of -1 comes before one of 0, which comes before 1, 2, 3, etc.

        This function is required to check that priority numbers are ints. """

        if not isinstance(priority, int): # check if priority is integer
            raise PriorityError("Priority must be an integer!")
        self._bHeap.insert((priority, self._index, val))
        self._index += 1
        
    def dequeue(self):
        """Removes and returns the highest priority value. 
        If multiple entries in the queue have the same priority, 
        those values are dequeued in the same order in which they were enqueued.

        This function is require to raise an exception if the queue is empty."""
        
        if len(self._bHeap.heap_list) <= 1:  # check if the queue is empty
            raise IndexError("Delete from an empty priority queue!")
        return self._bHeap.del_min()[-1]
    
# Test out the PriorityQueue to show it works as advertised.
p = PriorityQueue(5)
p.enqueue(1,0)
p.enqueue(2,2)
p.enqueue(3,1)
p.enqueue(4,1)
p.enqueue(5,5)
p.enqueue(6,-1)
p.enqueue(7,-1)
print(p._bHeap.heap_list)

for i in range(5):
    print(p.dequeue())