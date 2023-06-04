"""
Arrays are used to store a fixed number of elements of the same type. 
Unlike lists, arrays in Python are provided by the array module. They 
are more efficient when you are working with large amounts of numeric data.

"""

import array
my_array = array.array('i', [1, 2, 3, 4, 5])
my_array.append(6)
my_array.remove(2)

"""
A queue is a data structure that follows the First-In-First-Out (FIFO) principle.
The elements are inserted at the end (enqueue) and removed from the front (dequeue)
of the queue.

"""

from collections import deque
my_queue = deque()
my_queue.append(1)
my_queue.append(2)
item = my_queue.popleft()


"""
A stack is a data structure that follows the Last-In-First-Out (LIFO) principle. 
The elements are inserted and removed from the same end, known as the top of the stack. 
    
"""

my_stack = []
my_stack.append(1)
my_stack.append(2)
item = my_stack.pop()


"""
A linked list is a data structure consisting of a sequence of nodes, where each 
node contains a value and a reference to the next node. Linked lists are useful 
for dynamic data structures as they allow efficient insertion and deletion operations.

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.next = node3
