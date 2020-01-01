# Node of a doubly linked list  
class Node: 
    def __init__(self, next=None, prev=None, data=None): 
        self.next = next # reference to next node in DLL 
        self.prev = prev # reference to previous node in DLL 
        self.data = data

class DoublyLinkedList:

	def __init__(self):
		self.head = None

	# Adding a node at the front of the list 
	def push(self, new_data):

		# Allocate the Node & Put in the data 
	    new_node = Node(data = new_data) 
  
	    # Make next of new node as head and previous as NULL 
	    new_node.next = self.head 
	    new_node.prev = None
  
	    # 4. change prev of head node to new node  
	    if self.head is not None: 
	        self.head.prev = new_node 
  
	    # 5. move the head to point to the new node 
	    self.head = new_node

	# Given a node as prev_node, insert a new node after the given node 
	def insertAfter(self, prev_node, new_data):

		if prev_node is None:
			print('The given previous node does not exist')
			return

		# Allocate node and put in the data
		new_node = Node(data = new_data)
	
		# Make next of new node as next of prev_node
		new_node.next = prev_node.next	

		# Make the next of prev_node as new_node	
		prev_node.next = new_node
		
		# Make prev_node as previous of new_node
		new_node.prev = prev_node

		# Change previous of new_node's next node
		if new_node.next is not None:
	            new_node.next.prev = new_node

	# Given a reference to the head of DLL and integer, 
	# appends a new node at the end 
	def append(self, new_data): 
  
		# 1. Allocates node 
		# 2. Put in the data 
		new_node = Node(new_data) 
  
		# 3. This new node is going to be the last node, 
		# so make next of it as None 
		new_node.next = None
  
		# 4. If the Linked List is empty, then make the 
		# new node as head 
		if self.head is None: 
		    new_node.prev = None
		    self.head = new_node 
		    return 
  
		# 5. Else traverse till the last node 
		last = self.head 
		while(last.next is not None): 
		    last = last.next
  
		# 6. Change the next of last node 
		last.next = new_node 
  
		# 7. Make last node as previous of new node 
		new_node.prev = last 
  
		return

	# This function prints contents of linked list 
	# starting from the given node 
	def printList(self, node): 
  
		print("\nTraversal in forward direction")
		while(node is not None): 
		    print(node.data)
		    last = node 
		    node = node.next
  
		print("\nTraversal in reverse direction")
		while(last is not None): 
		    print(last.data)
		    last = last.prev

# Driver program to test above functions 
  
# Start with empty list 
llist = DoublyLinkedList() 
  
# Insert 6. So the list becomes 6->None 
llist.append(6) 
  
# Insert 7 at the beginning. 
# So linked list becomes 7->6->None 
llist.push(7) 
  
# Insert 1 at the beginning. 
# So linked list becomes 1->7->6->None 
llist.push(1) 
  
# Insert 4 at the end. 
# So linked list becomes 1->7->6->4->None 
llist.append(4) 
  
# Insert 8, after 7. 
# So linked list becomes 1->7->8->6->4->None 
llist.insertAfter(llist.head.next, 8) 
  
print("Created DLL is: ")
llist.printList(llist.head)			
