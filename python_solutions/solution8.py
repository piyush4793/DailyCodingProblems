# Problem 8:
# This problem was asked by Google

"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

# Author: Piyush Agarwal
# Written on: 02-01-2019

# Solution

"""
Explanation:
Inside helper function, the exit condition for recursive function is if root is None then return 0 and True
recursively check left and right subtree
if left subtree and right subtree is unival, then also match their value with current root value. If it matches with both subtrees, then only increase total count by 1
else return total count and False    => we won't add current subtree as unival since one of the left or right subtree is not unival
"""

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

# Also returns number of unival subtrees, and whether it is itself a unival subtree.
def helper(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.value != root.left.value:
            return total_count, False
        if root.right is not None and root.value != root.right.value:
            return total_count, False
        return total_count + 1, True
    return total_count, False

# Driver to run the solution

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

if __name__ == '__main__':
	root = Node(0)
	root.left = Node(1)
	root.right = Node(0)
	root.right.left = Node(1)
	root.right.right = Node(0)
	root.right.left.left = Node(1)
	root.right.left.right = Node(1)

	print(count_unival_subtrees(root))

	
