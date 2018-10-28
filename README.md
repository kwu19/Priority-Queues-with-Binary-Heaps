# Priority-Queues-with-Binary-Heaps

Implement a Priority Queue</font>

Implement a new class called `PriorityQueue`, based on the `BinaryHeap` class. The heap will be a **min heap**, meaning the smalles priority value is the root of the tree, and thus has the highest priority.

You have two objectives:

1. When creating a binary heap for your `PriorityQueue`, you will now **limit** the heap size. In other words, the heap only keeps track of the $n$ most important items. If the heap grows in size to more than $n$ items the least important item is *dropped*. 



2. Your `PriorityQueue` class should implement the following methods:
  * `__init__(n)`
  
     Initialize an empty priority queue, with a maximum size of n.
     <br/>
     <br/>

  * `enqueue(val, priority)`
  
     Adds `val` (any object, e.g. `str` or `int`) to the priority queue with the specified priority (an `int`). Smaller priority numbers correspond to higher priorities, which means that all priority 1 elements are dequeued before any priority 2 elements.

     Negative priorities are allowed and are not treated differently from other values. That is, a priority of -1 comes before one of 0, which comes before 1, 2, 3, etc.

     This function is **required** to check that priority numbers are `ints`. 
     <br/>
     <br/>
     
  * `dequeue`
  
     Removes and returns the highest priority value. If multiple entries in the queue have the same priority, those values are dequeued in the same order in which they were enqueued.

     This function is **require** to raise an exception if the queue is empty. 
