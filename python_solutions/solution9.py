# Problem 9:
# This problem was asked by Airbnb

"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""

# Author: Piyush Agarwal
# Written on: 31-12-2019

# Solution

def solve(arr):

	incl = 0
	excl = 0

	for elem in arr:
		new_excl = max(incl, excl) 
		 
		# Current max including elem
		incl = excl + elem
		excl = new_excl 
      
	# return max of incl and excl 
	return max(excl, incl)

print(solve([2, 4, 6, 2, 5]))
