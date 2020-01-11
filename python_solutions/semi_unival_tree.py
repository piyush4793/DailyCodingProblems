"""
Semi-unival tree:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

The tree is said to be semi unival if one of its child subtree has same value as root value 

"""

def count_semi_unival_subtrees(root):
	total_count, is_unival = helper(root)
	return total_count

def helper(root):
	if root is None:
		return 0, False
	
	left_count, is_left_unival = helper(root.left)
	right_count, is_right_unival = helper(root.right)


# Driver to run the solution

class Node:
        def __init__(self, value, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right

root = Node(0)
root.left = Node(1)
root.right = Node(0)
root.right.left = Node(1)
root.right.right = Node(0)
root.right.left.left = Node(1)
root.right.left.right = Node(1)

print(count_semi_unival_subtrees(root))
