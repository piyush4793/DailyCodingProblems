# Problem 1:
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Solution
# We can look for S-element in already traversed array
def solve(arr, s):
	elem_map = dict()
	for i in arr:
		if (s-i) in elem_map:
			return True
		else:
			elem_map[i] = 0
	return False

# Trying to find if there exists a pair of elements in the given array such that the sum is 17.
result = solve([10, 15, 3, 7], 170)
print(result)
