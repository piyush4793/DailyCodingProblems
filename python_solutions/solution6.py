# Problem 6:
# This problem was asked by Google

"""
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. 
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
"""

# Author: Piyush Agarwal
# Written on: 31-12-2019

# Solution

class DllNode:
	
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

class DoublyLinkedList:

	def __init__(self):
                self.head = None

	def add(self, data):
		self.head = Node()
		


class XorLinkedlist:

	def __init__(self):
		self.head = None

	def add(self, data):
		self.
