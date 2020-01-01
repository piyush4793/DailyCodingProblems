# Problem 4:
# This problem was asked by Stripe

"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

# Author: Piyush Agarwal
# Written on: 31-12-2019

# Solution

# Thought process:
# With no time constraint and space constraint
# Time: O(nlogn)
# Space: No auxiliary or extra space
def solve1(*args):
	"""
	    Sort the array and iterate through array while checking if the difference between two consecutive elements is 1.
	    Also ignore all non-positive numbers ( -ve and 0 ).
	    If the difference is not one, then break the loop and required answer will be previous element + 1.
	"""
	answer = []
	for arr in args:
		result = -1
		arr = sorted(arr) # Sort the array -> Time taken is O(nlogn)
		for idx, elem in enumerate(arr):
			if elem <= 0:
				continue
			else:
				if idx > 1 and arr[idx] - arr[idx-1] != 1:
					result = arr[idx-1] + 1
					break
		if result == -1:
			result = arr[-1] + 1 if arr[-1] > 0 else 1
		answer.append(result)
	print(f'Number of test cases: {len(args)}')
	print(answer)

# With linear time and no space constraint
# Time: O(n)
# Space: O(n)
def solve2(*args):
	"""
	   Maintain a dictionary to store all the positive elements of the array.
	   Iterate through array, add in dictionary if a positive element is encountered.
	   Iterate from 1 to max_element present in array. if any number is not found in dictionary that means it is the lowest positive number that we are looking for.
	   Edge case: if all elements in array are negative, then return 1 or if we have all the sequence present then the result will be next number to maximum element
	"""
	answer = []
	for arr in args:
		result = -1
		max_elem = max(arr)
		lookup_map = {}
		for elem in arr:
			if elem > 0:
				lookup_map[elem] = None

		for i in range(1, max_elem+1):
			if i not in lookup_map:
				result = i
				break

		if result == -1:
			result = max_elem + 1 if max_elem > 0 else 1
		answer.append(result)
	print(f'Number of test cases: {len(args)}')
	print(answer)

# With linear time and constant space
# Time: O(n)
# Space: O(1)
def solve3(*args):
	"""
	"""
	answer = []
	for arr in args:
		result = -1
		pos_filtered_arr = [i for i in arr if i > 0]
		
		# If array contains all non positive values
		if len(pos_filtered_arr)==0:
			answer.append(1)
			continue			

		"""
		 Marking the element as visited by marking arr[arr[i]-1] as negative
		 Make sure arr[i]-1 < (length of array - 1).
		 We don't need to worry about values that are larger than number of positive element because the missing number can never exceed the number of positive numbers present in the array
		 Example: [3, 4, -1, 1] 
		 Here number of positive elements in the given array is 3. So, least positive missing number cannot exceed 3
		"""
		pos_arr_len = len(pos_filtered_arr)
		for elem in pos_filtered_arr:
			abs_elem = abs(elem)
			if abs_elem <= pos_arr_len and pos_filtered_arr[abs_elem-1] > 0:
				# Change element to negative value
				pos_filtered_arr[abs_elem-1] = -pos_filtered_arr[abs_elem-1]

		for idx, elem in enumerate(pos_filtered_arr):
			if elem > 0:
				result = idx + 1
				break

		if result == -1:
			result = pos_arr_len + 1
		answer.append(result)
	print(f'Number of test cases: {len(args)}')
	print(answer)
	

solve1([3, 4, -1, 1], [1, 2, 0], [-2, -3, 0], [4, 3, 2, 1])
solve2([3, 4, -1, 1], [1, 2, 0], [-2, -3, 0], [4, 3, 2, 1])
solve3([3, 4, -1, 1], [1, 2, 0], [-2, -3, 0], [4, 3, 2, 1])
